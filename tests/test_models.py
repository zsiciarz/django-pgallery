from __future__ import unicode_literals

import unittest

from django.test import TestCase

from pgallery.models import Gallery, Photo
from .factories import GalleryFactory, PhotoFactory


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

    def test_for_exif(self):
        photo = PhotoFactory(exif={'Make': 'Canon'})
        self.assertIn(photo, Photo.objects.for_exif('Make', 'Canon'))

    def test_for_exif_negative(self):
        photo = PhotoFactory(exif={'Make': 'Nikon'})
        self.assertNotIn(photo, Photo.objects.for_exif('Make', 'Canon'))

    def test_popular_tags(self):
        PhotoFactory(tags=['cat'])
        PhotoFactory(tags=['cat', 'fail'])
        PhotoFactory(tags=['dog', 'cat', 'fail'])
        tags = Photo.objects.popular_tags(count=3)
        self.assertEqual(tags, [
            {'count': 3, 'tag': 'cat'},
            {'count': 2, 'tag': 'fail'},
            {'count': 1, 'tag': 'dog'},
        ])

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
