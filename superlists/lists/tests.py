from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_resolves_to_home_page_view(self):
        # resolve is a function Django uses internally to resolve URLs
        found = resolve('/')
        self.assertEqual(found.func, home_page)
