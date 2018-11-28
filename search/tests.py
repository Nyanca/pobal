from django.test import TestCase
from django.http import HttpResponse
import json

class TestSearchView(TestCase):
    def test_search_route_renders_expected_response(self):
        # show that empty request doers not return template
        page = self.client.get('/search/')
        self.assertEqual(page.content, (b'Please submit a search term.'))
        self.assertTemplateNotUsed(page, 'all_tickets.html')
