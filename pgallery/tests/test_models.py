from __future__ import unicode_literals

import unittest

from django.conf import settings
from django.test import TestCase

import factory

from ..models import Gallery, Photo


class UserFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = settings.AUTH_USER_MODEL


class GalleryFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Gallery
    author = factory.SubFactory(UserFactory)


class PhotoFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Photo
    gallery = factory.SubFactory(GalleryFactory)
    author = factory.LazyAttribute(lambda obj: obj.gallery.author)
    image = factory.django.ImageField(width=1024, height=768)


class GalleryModelTestCase(unittest.TestCase):
    """
    Tests for ``Gallery`` model class.
    """

    def test_str(self):
        """
        Check that string representation of a gallery is its title.
        """
        gallery = Gallery(title="Test gallery")
        self.assertEqual(str(gallery), gallery.title)


class GalleryModelIntegrationTestCase(TestCase):
    """
    Tests for ``Gallery`` model that require database connection.
    """
    def test_unpublished_galleries(self):
        gallery = GalleryFactory(status='draft')
        self.assertNotIn(gallery, Gallery.objects.published())

    def test_published_galleries(self):
        gallery = GalleryFactory(status='published')
        self.assertIn(gallery, Gallery.objects.published())


class PhotoModelTestCase(unittest.TestCase):
    """
    Tests for ``Photo`` model class.
    """

    def test_str(self):
        """
        Check that string representation of a photo is its title.
        """
        photo = Photo(title="Test photo")
        self.assertEqual(str(photo), photo.title)
