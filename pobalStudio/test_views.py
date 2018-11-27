from django.test import TestCase
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Ticket
from .views import pobal_studio, ticket_form, get_all_tickets, ticket_detail, ticket_like_toggle, add_comment, create_or_edit_ticket, delete_ticket
from .forms import CommentForm

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
        
    def test_create_or_edit_ticket_form_for_idNONE(self):
        # test that 404 error is raised if ticket not found
        page = self.client.get('/pobal_studio/1/edit/')
        self.assertEqual(page.status_code, 404)
        print('test_create_or_edit_ticket_form_for_NONE_route: Cannot edit ticket. Ticket does not exist')

    def test_delete_ticket_route(self):
        ticket = Ticket(title='a ticket', summary='a ticket summary', detail='ticket detail')
        ticket.save()
        
        page = self.client.get('/pobal_studio/{0}/delete/'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_tickets.html')
        
class OtherOtherFeatures(TestCase):
    def test_timezone_now(self):
        # compare the date stamp on two tickets saved one after the other 
        ticket = Ticket(title='a ticket', summary='a ticket summary', detail='ticket detail')
        ticket.save()
        
        ticket2 = Ticket(title='a 2nd ticket', summary='a 2nd ticket summary', detail='more ticket detail')
        ticket2.save()
        self.assertTrue(ticket.date < ticket2.date)
        
    def test_view_incrementation_on_page_load(self):
        # create ticket for accessing urls that contain ticket id's
        ticket = Ticket(title='a ticket', summary='a ticket summary', detail='ticket detail')
        ticket.save()
        
        # get ticket_detail page by ticket id created above
        page = self.client.get('/pobal_studio/{0}/'.format(ticket.id))
        
        # hardcode page load to test view incrementation functionality    
        if self.assertTemplateUsed(page, 'ticket_detail.html') is True:
            ticket.views += 1
            self.assertEqual(ticket.views, 1)
    
        