# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2012-2016.

from __future__ import unicode_literals

from PIL import Image, ExifTags

from django.conf import settings
from django.contrib.postgres.fields import ArrayField, HStoreField
from django.db import connection, models
from django.db.models.query import QuerySet
from django.utils.encoding import python_2_unicode_compatible
from django.utils import six
from django.utils.translation import ugettext_lazy as _

from markitup.fields import MarkupField
from model_utils import Choices
from model_utils.models import StatusModel, TimeStampedModel


def sanitize_exif_value(key, value):
    if isinstance(value, six.string_types):
        return value.replace('\x00', '').strip()
    return str(value)


class GalleryQuerySet(QuerySet):
    def published(self):
        return self.filter(status='published')


@python_2_unicode_compatible
class Gallery(StatusModel, TimeStampedModel):
    STATUS = Choices(
        ('draft', _("draft")),
        ('published', _("published")),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, verbose_name=_("author"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), max_length=255, unique=True)
    description = MarkupField(_("description"))
    shot_date = models.DateField(_("shot date"), null=True, blank=True)
    cover_photo = models.ImageField(_("cover photo"), upload_to='photos/%Y/%m/%d', null=True, blank=True)

    objects = GalleryQuerySet.as_manager()

    class Meta:
        verbose_name_plural = _("Galleries")
        ordering = ['-shot_date']

    def __str__(self):
        """
        The string representation of a gallery is its title.
        """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('pgallery:gallery_details', [], {'slug': self.slug})

    def get_teaser_photos(self):
        return self.photos.all()[:4]


class PhotoManager(models.Manager):
    def tagged(self, tag):
        return self.filter(tags__contains=[tag]).order_by('-gallery__shot_date')

    def for_exif(self, exif_key, exif_value):
        return self.filter(exif__contains={exif_key: exif_value}).order_by('-gallery__shot_date')

    def popular_tags(self, count=10):
        query = """
        select
            t.tag,
            count(t.tag) as tag_count
        from
            (select unnest(tags) as tag from %s) t
        group by tag
        order by tag_count desc
        limit %%s
        """ % Photo._meta.db_table
        cursor = connection.cursor()
        cursor.execute(query, (count,))
        tags = [{'tag': row[0], 'count': row[1]} for row in cursor.fetchall()]
        return tags


@python_2_unicode_compatible
class Photo(TimeStampedModel):
    gallery = models.ForeignKey(Gallery, null=True, related_name='photos', verbose_name=_("gallery"), on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, verbose_name=_("author"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=255)
    image = models.ImageField(_("image"), upload_to='photos/%Y/%m/%d')
    tags = ArrayField(models.CharField(max_length=64), blank=True, default=list)
    exif = HStoreField(editable=False, default={}, db_index=True)

    objects = PhotoManager()

    class Meta:
        verbose_name_plural = _("Photos")
        ordering = ['created']

    def __str__(self):
        """
        The string representation of a photo is its title.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Updates EXIF data before saving.
        """
        # you really should be doing this in a background task
        try:
            img = Image.open(self.image.file)
            raw_exif = img._getexif()
            if raw_exif:
                self.exif = {ExifTags.TAGS[k]: sanitize_exif_value(k, v) for k, v in raw_exif.items() if k in ExifTags.TAGS}
        except Exception:
            pass
        super(Photo, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('pgallery:photo_details', [], {'pk': self.pk})

    def get_next_photo(self):
        """
        Returns next photo from the same gallery (in chronological order).

        Wraps around from last photo in the gallery to the first one.
        """
        try:
            next_photo = Photo.objects.filter(
                gallery=self.gallery,
                created__gt=self.created,
            )[0]
        except IndexError:
            next_photo = Photo.objects.filter(gallery=self.gallery)[0]
        return next_photo

    def get_previous_photo(self):
        """
        Returns previous photo from the same gallery (in chronological order).

        Wraps around from first photo in the gallery to the last one.
        """
        try:
            previous_photo = Photo.objects.filter(
                gallery=self.gallery,
                created__lt=self.created,
            ).latest('created')
        except Photo.DoesNotExist:
            previous_photo = Photo.objects.filter(gallery=self.gallery).latest('created')
        return previous_photo
