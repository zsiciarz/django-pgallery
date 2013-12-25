from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase

from djet.files import create_inmemory_image

from ..models import Gallery, Photo


class BaseTestCase(TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()
        User = get_user_model()
        self.user = User.objects.create_user(
            username='test',
            email='test@example.org',
            password='test',
        )
        self.gallery = Gallery.objects.create(
            author=self.user,
            title="Test gallery",
            slug="test-gallery",
        )
        self.photo = Photo.objects.create(
            gallery=self.gallery,
            author=self.user,
            title="Test photo",
            image=create_inmemory_image('test.jpg', format='JPEG'),
            exif={},
        )


class GalleryModelTestCase(BaseTestCase):
    """
    Tests for ``Gallery`` model class.
    """

    def test_str(self):
        """
        Check that string representation of a gallery is its title.
        """
        self.assertEqual(str(self.gallery), self.gallery.title)


class PhotoModelTestCase(BaseTestCase):
    """
    Tests for ``Photo`` model class.
    """

    def test_str(self):
        """
        Check that string representation of a photo is its title.
        """
        self.assertEqual(str(self.photo), self.photo.title)
