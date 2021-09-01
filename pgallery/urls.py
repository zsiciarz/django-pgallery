from django.urls import re_path

from .feeds import GalleryFeed
from .views import (
    GalleryListView,
    GalleryMonthArchiveView,
    GalleryDetailsView,
    TaggedPhotoListView,
    ExifPhotoListView,
    PhotoDetailsView,
)


app_name = "pgallery"

urlpatterns = [
    re_path(route=r"^$", view=GalleryListView.as_view(), name="gallery_list"),
    re_path(route=r"^rss/$", view=GalleryFeed(), name="gallery_rss"),
    re_path(
        route=r"^photo/(?P<pk>\d+)/$",
        view=PhotoDetailsView.as_view(),
        name="photo_details",
    ),
    re_path(
        route=r"^tag/(?P<tag>[ \w]+)/$",
        view=TaggedPhotoListView.as_view(),
        name="tagged_photo_list",
    ),
    re_path(
        route=r"^exif/(?P<exif_key>[ \w]+)/(?P<exif_value>.+)/$",
        view=ExifPhotoListView.as_view(),
        name="exif_photo_list",
    ),
    re_path(
        route=r"^(?P<slug>[-\w]+)/$",
        view=GalleryDetailsView.as_view(),
        name="gallery_details",
    ),
    re_path(
        route=r"^(?P<year>\d{4})/(?P<month>\d+)/$",
        view=GalleryMonthArchiveView.as_view(),
        name="month_archive",
    ),
]
