from django.contrib.sitemaps import Sitemap

from .models import Gallery, Photo


class GallerySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Gallery.published.all()

    def lastmod(self, obj):
        return obj.modified


class PhotoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Photo.objects.all()

    def lastmod(self, obj):
        return obj.modified
