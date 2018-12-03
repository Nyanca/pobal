from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Ticket, Comment

class TestTicketModel(TestCase):
    def test_title_is_a_str(self):
        test_title = Ticket(title = 'A Ticket')
        self.assertEqual(str(test_title), 'A Ticket')

    def test_title_max_length_is_50(self):
        test_ticket = Ticket(title = ('x' * 51), summary='a summary', detail='some details')
        test_ticket.save()
        self.assertRaises({'max_length': 'Ensure this value has at most 50 characters(it has 51). '})
        print('test_title_max_length_is_50: max char field has been exceeded')
        
    def test_summary_max_length_is_100(self):
        test_ticket = Ticket(title = 'a ticket', summary=('x' * 101), detail='some details')
        test_ticket.save()
        self.assertRaises({'max_length': 'Ensure this value has at most 100 characters(it has 101). '})
        print('test_summary_max_length_is_100: max char field has been exceeded')
    
    def test_price_defaults_to_500(self):
        test_ticket = Ticket(title = 'a ticket', summary='a test summary', detail='some detail')
        test_ticket.save()
        self.assertEqual(test_ticket.price, 500.0)
        
    def test_views_defaults_to_0(self):
        test_ticket = Ticket(title = 'a ticket', summary='a test summary', detail='some detail')
        test_ticket.save()
        self.assertEqual(test_ticket.views, 0)
