from __future__ import unicode_literals

import unittest

from ..models import sanitize_exif_value


class SanitizeExifValueTestCase(unittest.TestCase):
    def test_strip_null_bytes(self):
        """
        Check that null bytes are stripped from the string.
        """
        key = "not relevant"
        value = "abc\x00d"
        self.assertEqual(sanitize_exif_value(key, value), "abcd")
