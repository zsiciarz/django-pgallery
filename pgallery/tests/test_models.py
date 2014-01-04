from __future__ import unicode_literals

import unittest

from ..models import Gallery, Photo


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
