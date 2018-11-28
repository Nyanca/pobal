from django.test import TestCase
from django.http import HttpResponse
import json

class TestSearchView(TestCase):
    def test_search_route_renders_expected_response(self):
        # show that empty request doers not return template
        page = self.client.get('/search/')
        self.assertEqual(page.content, (b'Please submit a search term.'))
        self.assertTemplateNotUsed(page, 'all_tickets.html')
        
    def test_search_route_renders_expected_template(self):
        # show that request returns template when vaue 'q' is found
        response = self.client.get('/search/', {'q': 'a value'})
        self.assertTemplateUsed(response, 'all_tickets.html')
