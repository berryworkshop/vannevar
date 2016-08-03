from django.test import TestCase
from django.test import Client


class HomeTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.response = self.client.get('/')

    def test_home_response(self):
        self.assertEqual(self.response.status_code, 200)


class CollectionOrganizationsTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.response = self.client.get('/collection/organizations/')

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)
