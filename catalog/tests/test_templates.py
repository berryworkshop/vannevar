from django.test import TestCase
from django.test import Client
from catalog.models import Organization
from model_mommy import mommy


class HomeTest(TestCase):
    def setUp(self):
        '''
        Create a test client.
        '''
        self.client = Client()
        self.response = self.client.get('/')

    def test_home_response(self):
        '''
        Response should be successful.
        '''
        self.assertEqual(self.response.status_code, 200)

    def test_template_used_is_home(self):
        '''
        Response should use the correct template.
        '''
        self.assertTemplateUsed(self.response, 'cms/home.html')


class CatalogOrganizationsTest(TestCase):

    def setUp(self):
        '''
        Create some organizations to use in tests, and a test client.
        '''
        self.orgs = [
            {'name': 'The Art Institute of Chicago'},
            {'name': 'The University of Illinois at Chicago'},
            {'name': 'Online Computer Library Center, Inc.'},
        ]
        for org in self.orgs:
            mommy.make(Organization, name=org['name'])

        self.client = Client()
        self.response = self.client.get('/catalog/organizations/')

    def test_index_response(self):
        '''
        Response should be successful.
        '''
        self.assertEqual(self.response.status_code, 200)

    def test_template_used_is_organizations(self):
        '''
        Response should use the correct template.
        '''
        self.assertTemplateUsed(self.response, 'catalog/organizations.html')


