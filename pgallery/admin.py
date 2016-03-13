# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2012-2016.

from __future__ import unicode_literals

"""
Administration for photos and galleries.
"""

from django.contrib import admin
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from .forms import PhotoForm
from .models import Gallery, Photo


class PhotoInline(admin.TabularInline):
    """
    Administration for photos.
    """
    model = Photo
    form = PhotoForm
    ordering = ['created']

    def get_extra(self, request, obj=None, **kwargs):
        return 0 if obj else 3


class GalleryAdmin(admin.ModelAdmin):
    """
    Administration for galleries.
    """
    list_display = (
        'author', 'title', 'status', 'description', 'shot_date', 'modified',
        'photo_count',
    )
    list_display_links = ('title',)
    list_editable = ('status',)
    list_filter = ('status',)
    date_hierarchy = 'shot_date'
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoInline]

    def photo_count(self, obj):
        return obj.photo_count
    photo_count.short_description = _("Photo count")

    def get_queryset(self, request):
        """
        Add number of photos to each gallery.
        """
        qs = super(GalleryAdmin, self).get_queryset(request)
        return qs.annotate(photo_count=Count('photos'))

    def save_model(self, request, obj, form, change):
        """
        Set currently authenticated user as the author of the gallery.
        """
        obj.author = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        """
        For each photo set it's author to currently authenticated user.
        """
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, Photo):
                instance.author = request.user
            instance.save()


admin.site.register(Gallery, GalleryAdmin)
