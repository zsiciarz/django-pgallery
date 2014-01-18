from __future__ import unicode_literals

import unittest

from django.conf import settings

import factory

from ..models import Gallery, Photo


class UserFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = settings.AUTH_USER_MODEL


class GalleryFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Gallery
    author = factory.SubFactory(UserFactory)


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
