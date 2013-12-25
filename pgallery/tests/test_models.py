from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase

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


class GalleryModelTestCase(BaseTestCase):
    """
    Tests for ``Gallery`` model class.
    """

    def test_str(self):
        """
        Check that string representation of a gallery is its title.
        """
        self.assertEqual(str(self.gallery), self.gallery.title)
