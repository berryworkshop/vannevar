from django.test import TestCase
from .models import Organization

class OrganizationTestCase(TestCase):
    def setUp(self):
        Organization.objects.create(name="Test Org")

    def test_org_str(self):
        '''
        Organizations provide accurate string representation.
        '''
        org = Organization.objects.get(name="Test Org")
        self.assertEqual(org.__str__(), 'Test Org')


    def test_org_to_json(self):
        '''
        Organizations provide json representation, with all required keys.
        '''
        org = Organization.objects.get(name="Test Org")
        self.assertTrue('id' in org.to_json())
        self.assertTrue('slug' in org.to_json())
        self.assertTrue('created' in org.to_json())
        self.assertTrue('modified' in org.to_json())
        self.assertTrue('class_name' in org.to_json())
