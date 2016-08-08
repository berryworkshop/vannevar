from django.test import TestCase
from catalog.models import Organization
from model_mommy import mommy


class OrganizationTestCase(TestCase):

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

    def test_org_str(self):
        '''
        Organizations provide accurate string representation.
        '''
        org = Organization.objects.get(name="The Art Institute of Chicago")
        self.assertEqual(org.__str__(), 'The Art Institute of Chicago')

    def test_org_to_json(self):
        '''
        Organizations provide json representation, with all required keys.
        '''
        org = Organization.objects.get(name="The Art Institute of Chicago")
        self.assertTrue('id' in org.to_json())
        self.assertTrue('slug' in org.to_json())
        self.assertTrue('created' in org.to_json())
        self.assertTrue('modified' in org.to_json())
        self.assertTrue('class_name' in org.to_json())
