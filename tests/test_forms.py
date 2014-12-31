from __future__ import unicode_literals

import unittest

from pgallery.forms import PhotoForm


class PhotoFormTestCase(unittest.TestCase):
    def test_form_invalid(self):
        form = PhotoForm({})
        self.assertFalse(form.is_valid())
