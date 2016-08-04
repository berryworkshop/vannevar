from wagtail.tests.utils import WagtailPageTests
from django.test import Client
from wagtail.wagtailcore.models import Page 
from .models import ArticlePage, ArticleIndexPage, HomePage

class MyPageTests(WagtailPageTests):

    def setUp(self):
        '''
        # Create a test client.
        '''
        self.client = Client()
        self.response = self.client.get('/')

        # self.root_page = Page.get_first_root_node()
        self.home_page = Page.objects.get(slug='home')

    def test_can_create_a_page(self):
        # Create a page instance with all the required fields populated,
        # but not yet saved to the database 
        page = ArticlePage(
            title="Test page.",
            slug="test-page",
            ) 
        self.home_page.add_child(instance=page) 

        response = self.client.get('/test-page/')
        self.assertEqual(response.status_code, 200)