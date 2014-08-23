from ..models import Project
from .models import Links

from ..base import TestCase


class LinksTests(TestCase):

    def setUp(self):
        self.project = Project.objects.create()
        self.links = Links.objects.create()

    def test_related_accessor(self):
        self.links.related_objects.add(self.project)
        self.links.save()
        self.assertEqual(self.project.related_links.count(), 1)
        self.assertIn(self.links, self.project.related_links.all())
