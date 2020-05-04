from django.test import TestCase


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        # test implementation
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
