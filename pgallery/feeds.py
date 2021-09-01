"""
Gallery syndication feeds.
"""

from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from .models import Gallery


class GalleryFeed(Feed):
    """
    RSS feed with latest galleries.
    """

    title = _("siciarz.net - galleries")
    link = reverse_lazy("pgallery:gallery_list")
    description = _("Latest photo galleries")

    def items(self):
        return Gallery.objects.published()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
