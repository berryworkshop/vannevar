from django.test import TestCase
from django.test import Client
from catalog.models import Organization
from model_mommy import mommy
import json


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
            {'name': 'The Art Institute of Chicago', 'slug': 'artic'},
            {'name': 'The University of Illinois at Chicago', 'slug': 'uic'},
            {'name': 'Online Computer Library Center, Inc.', 'slug': 'oclc'},
        ]
        for org in self.orgs:
            mommy.make(Organization, name=org['name'], slug=org['slug'])

        client = Client()
        self.response = self.client.get('/organizations/')

    def test_page(self):
        '''
        Index page should load and use the correct template.
        '''
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'catalog/organizations.html')

    def test_json(self):
        '''
        Organizations index json pages should load, be JSON,
        and be longer than a single record.
        '''
        response = self.client.get('/organizations/?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
        self.assertTrue(len(response.json()) > 1)


class CatalogSingleOrganizationTest(TestCase):

    def setUp(self):
        '''
        Create some organizations to use in tests, and a test client.
        '''
        self.orgs = [
            # provide several to choose from
            {'name': 'The Art Institute of Chicago', 'slug': 'artic'},
            {'name': 'The University of Illinois at Chicago', 'slug': 'uic'},
            {'name': 'Online Computer Library Center, Inc.', 'slug': 'oclc'},
        ]
        for org in self.orgs:
            mommy.make(Organization, name=org['name'], slug=org['slug'])

        client = Client()
        self.org = Organization.objects.get(slug="artic")
        self.response = self.client.get(
            '/organizations/{}'.format(self.org.slug))

    def test_page(self):
        '''
        Organization page should load, be unique, and use the correct template.
        '''
        self.assertEqual(self.response.status_code, 200)
        second_response = self.client.get(
            '/organizations/{}'.format('oclc'))
        self.assertNotEqual(self.response.content, second_response.content)
        self.assertTemplateUsed(self.response, 'catalog/organization.html')

    def test_json(self):
        '''
        Organization.json pages should load, be JSON, and be a single record.
        '''
        json_response = self.client.get(
            '/organizations/{}?format=json'.format(self.org.slug))
        self.assertEqual(json_response.status_code, 200)
        self.assertTrue(json_response.json())
        self.assertEqual(json_response['Content-Type'], 'application/json')
        self.assertTrue(len(json_response.json()) == 1)