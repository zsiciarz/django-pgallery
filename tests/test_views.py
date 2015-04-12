from __future__ import unicode_literals

from djet.testcases import ViewTestCase

from pgallery.views import TaggedPhotoListView


class TaggedPhotoListViewTestCase(ViewTestCase):
    view_class = TaggedPhotoListView

    def test_tag_in_response(self):
        request = self.factory.get()
        response = self.view(request, tag='example_tag')
        self.assertContains(response, 'example_tag')
