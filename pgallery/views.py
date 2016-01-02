# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2012-2016.

from __future__ import unicode_literals

from django.views.generic import ListView, DetailView, MonthArchiveView

from .models import Gallery, Photo


class StaffAccessMixin(object):
    """
    Allow staff members to see all galleries, including drafts.
    """
    def get_queryset(self):
        if self.request.user.is_staff:
            return Gallery.objects.all()
        return Gallery.objects.published()


class GalleryListView(StaffAccessMixin, ListView):
    pass


class GalleryMonthArchiveView(StaffAccessMixin, MonthArchiveView):
    date_field = 'shot_date'
    month_format = '%m'
    make_object_list = True


class GalleryDetailsView(StaffAccessMixin, DetailView):
    pass


class TaggedPhotoListView(ListView):
    def get_queryset(self):
        return Photo.objects.tagged(self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        data = super(TaggedPhotoListView, self).get_context_data(**kwargs)
        data['tag'] = self.kwargs['tag']
        return data


class ExifPhotoListView(ListView):
    template_name = 'pgallery/exif_photo_list.html'

    def get_queryset(self):
        return Photo.objects.for_exif(self.kwargs['exif_key'], self.kwargs['exif_value'])

    def get_context_data(self, **kwargs):
        data = super(ExifPhotoListView, self).get_context_data(**kwargs)
        data['exif_key'] = self.kwargs['exif_key']
        data['exif_value'] = self.kwargs['exif_value']
        return data


class PhotoDetailsView(DetailView):
    model = Photo
