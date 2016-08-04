from django.test import TestCase
from django.test import Client
from collection.models import Organization
from model_mommy import mommy


class HomeTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.response = self.client.get('/')

    def test_home_response(self):
        self.assertEqual(self.response.status_code, 200)


class CollectionOrganizationsTest(TestCase):

    def setUp(self):
        self.orgs = [
            'The Art Institute of Chicago',
            'The University of Illinois at Chicago',
            'Online Computer Library Center, Inc.',
        ]
        for org in self.orgs:
            mommy.make(Organization, name=org)

        self.client = Client()
        self.response = self.client.get('/collection/organizations/')

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used_is_organizations(self):
        self.assertTemplateUsed(self.response, 'collection/organizations.html')

    def test_organizations_headline(self):
        self.assertContains(self.response,
            '<h1>List of Organizations.</h1>',
            html=True,
            )

    def test_organizations_list(self):
        for org in self.orgs:
            self.assertContains(self.response,
                '<li>{}</li>'.format(org),
                html=True
                )
