from django.test import TestCase
from django.shortcuts import render, reverse, get_object_or_404
from .models import Ticket
from .views import pobal_studio, ticket_form, get_all_tickets, ticket_detail, ticket_like_toggle, add_comment, create_or_edit_ticket, delete_ticket

class TestViewRoutes(TestCase):
    def test_get_ticket_form_route(self):
        page = self.client.get('/pobal_studio/ticket_form/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'ticket_form.html')
        
    def test_get_all_tickets_route(self):
        page = self.client.get('/pobal_studio/tickets/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_tickets.html')
        
    def test_get_ticket_detail_route(self):
        ticket = Ticket(title='a ticket', summary='a ticket summary', detail='ticket detail')
        ticket.save()
        
        page = self.client.get('/pobal_studio/{0}/'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'ticket_detail.html')
        
    def test_get_comment_form_route(self):
        ticket = Ticket(title='a ticket', summary='a ticket summary', detail='ticket detail')
        ticket.save()
        
        page = self.client.get('/pobal_studio/{0}/comment/'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'comment_form.html')
    
    def test_create_or_edit_ticket_form_route(self):
        ticket = Ticket(title='a ticket', summary='a ticket summary', detail='ticket detail')
        ticket.save()
        
        page = self.client.get('/pobal_studio/{0}/edit/'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'ticket_form.html')
        
    def test_delete_ticket_route(self):
        ticket = Ticket(title='a ticket', summary='a ticket summary', detail='ticket detail')
        ticket.save()
        
        page = self.client.get('/pobal_studio/{0}/delete/'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_tickets.html')
    
    
        
        
    