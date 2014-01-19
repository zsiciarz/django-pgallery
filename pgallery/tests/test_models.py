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

    def test_teaser_photos(self):
        gallery = GalleryFactory()
        for i in range(3):
            PhotoFactory(gallery=gallery)
        self.assertEqual(len(gallery.get_teaser_photos()), 3)

    def test_teaser_photos_max_number(self):
        gallery = GalleryFactory()
        for i in range(7):
            PhotoFactory(gallery=gallery)
        self.assertEqual(len(gallery.get_teaser_photos()), 4)


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


class PhotoModelIntegrationTestCase(TestCase):
    """
    Tests for ``Photo`` model that require database connection.
    """
    def test_not_tagged(self):
        photo = PhotoFactory(tags=['tag1', 'tag2'])
        self.assertNotIn(photo, Photo.objects.tagged('tag3'))

    def test_tagged(self):
        photo = PhotoFactory(tags=['tag1', 'tag2'])
        self.assertIn(photo, Photo.objects.tagged('tag2'))

    def test_next_photo(self):
        gallery = GalleryFactory()
        photo1 = PhotoFactory(gallery=gallery)
        photo2 = PhotoFactory(gallery=gallery)
        self.assertEqual(photo1.get_next_photo(), photo2)

    def test_next_photo_wraparound(self):
        gallery = GalleryFactory()
        photo1 = PhotoFactory(gallery=gallery)
        photo2 = PhotoFactory(gallery=gallery)
        self.assertEqual(photo2.get_next_photo(), photo1)

    def test_next_photo_single(self):
        photo = PhotoFactory()
        self.assertEqual(photo.get_next_photo(), photo)

    def test_previous_photo(self):
        gallery = GalleryFactory()
        photo1 = PhotoFactory(gallery=gallery)
        photo2 = PhotoFactory(gallery=gallery)
        self.assertEqual(photo2.get_previous_photo(), photo1)

    def test_previous_photo_wraparound(self):
        gallery = GalleryFactory()
        photo1 = PhotoFactory(gallery=gallery)
        photo2 = PhotoFactory(gallery=gallery)
        self.assertEqual(photo1.get_previous_photo(), photo2)

    def test_previous_photo_single(self):
        photo = PhotoFactory()
        self.assertEqual(photo.get_previous_photo(), photo)
