# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2012-2016.

from __future__ import unicode_literals

from django.conf.urls import url

from .feeds import GalleryFeed
from .views import GalleryListView, GalleryMonthArchiveView, \
    GalleryDetailsView, TaggedPhotoListView, ExifPhotoListView, PhotoDetailsView


app_name = 'pgallery'

urlpatterns = [
    url(
        regex=r'^$',
        view=GalleryListView.as_view(),
        name='gallery_list'
    ),
    url(
        regex=r'^rss/$',
        view=GalleryFeed(),
        name='gallery_rss'
    ),
    url(
        regex=r'^photo/(?P<pk>\d+)/$',
        view=PhotoDetailsView.as_view(),
        name='photo_details'
    ),
    url(
        regex=r'^tag/(?P<tag>[ \w]+)/$',
        view=TaggedPhotoListView.as_view(),
        name='tagged_photo_list'
    ),
    url(
        regex=r'^exif/(?P<exif_key>[ \w]+)/(?P<exif_value>.+)/$',
        view=ExifPhotoListView.as_view(),
        name='exif_photo_list'
    ),
    url(
        regex=r'^(?P<slug>[-\w]+)/$',
        view=GalleryDetailsView.as_view(),
        name='gallery_details'
    ),
    url(
        regex=r'^(?P<year>\d{4})/(?P<month>\d+)/$',
        view=GalleryMonthArchiveView.as_view(),
        name='month_archive'
    ),
]
