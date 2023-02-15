from django.test import TestCase, SimpleTestCase


class SimpleTest(SimpleTestCase):
    
    def test_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)