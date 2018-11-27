from django.test import TestCase
from .forms import CreateTicketForm, CommentForm

class TestCreateTicketForm(TestCase):
    def test_can_create_ticket_with_only_required_fields(self):
        form = CreateTicketForm({'title':'a test ticket', 'summary':'a ticket test summary', 'detail':'some detail for testing purposes'})
        self.assertTrue(form.is_valid())
        
    def test_error_raised_with_invalid_form_input(self):
        form = CreateTicketForm({'title':'a test ticket'})
        self.assertRaises(Exception, [u'This field cannot be blank.'])
    
    def test_price_field_only_takes_int_value(self):
        form = CreateTicketForm({'price':'one hundred and fifty'})
        self.assertRaises(Exception, [u'This field must be an integer value.'])
        print('test_price_field_only_takes_int_value: The price must be entered as numbers, and not letters!')
        
    def test_price_field_only_takes_two_floats(self):
        form = CreateTicketForm({'price':0.123})
        self.assertFalse(form.is_valid())
        print('test_price_field_only_takes_int_value: The price field has been given more than 2 decimal places')

class TestCommentForm(TestCase):
    def test_that_comment_form_must_contain_a_comment(self):
        form = CommentForm({'comment':''})
        self.assertRaises(Exception, [u'This field cannot be blank.'])
        print('test_that_comment_form_must_contain_a_comment: No comment has been entered')
        
    def test_that_comment_form_requires_only_one_field(self):
        form = CommentForm({'comment':'a single comment for testing'})
        self.assertTrue(form.is_valid())
        
    def test_that_comment_form_takes_int_and_special_characters(self):
        form = CommentForm({'comment':'%7&**'})
        self.assertTrue(form.is_valid())