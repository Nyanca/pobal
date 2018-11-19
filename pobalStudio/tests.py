from django.test import TestCase
from .models import Ticket, Comment

class TicketTests(TestCase):
    def test_str(self):
        test_name = Ticket(title = 'A Ticket')
        self.assertEqual(str(test_name), 'A Ticket')