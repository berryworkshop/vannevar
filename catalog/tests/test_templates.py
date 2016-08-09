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
            {'name': 'The Art Institute of Chicago', 'slug': 'artic'},
            {'name': 'The University of Illinois at Chicago', 'slug': 'uic'},
            {'name': 'Online Computer Library Center, Inc.', 'slug': 'oclc'},
        ]
        for org in self.orgs:
            mommy.make(Organization, name=org['name'], slug=org['slug'])

        client = Client()
        self.response = self.client.get('/catalog/organizations/')

    def test_orgs_index(self):
        '''
        Index page should load.
        '''
        self.assertEqual(self.response.status_code, 200)

    def test_orgs_index(self):
        '''
        Response should use correct template.
        '''
        self.assertTemplateUsed(self.response, 'catalog/organizations.html')

    def test_org_pages(self):
        '''
        Individual Organization pages should load.
        '''
        orgs = Organization.objects.all()
        for org in orgs:
            response = self.client.get('/catalog/organizations/{}'.format(org.slug))
            try:
                self.assertEqual(response.status_code, 200)
            except AssertionError as e:
                raise AssertionError(
                    '{}: "/catalog/organizations/{}/"'.format(e, org.slug))

    def test_org_page_templates(self):
        '''
        Individual Organization pages should use the organization template.
        '''
        org = Organization.objects.get(slug="artic")
        response = self.client.get('/catalog/organizations/{}'.format(org.slug))
        self.assertTemplateUsed(response, 'catalog/organization.html')

    def test_org_json(self):
        '''
        Organization.json pages should load and use the JSON API.
        '''
        org = Organization.objects.get(slug="artic")
        response = self.client.get('/catalog/organizations/{}?format=json'.format(org.slug))
        self.assertEqual(response.status_code, 200)

