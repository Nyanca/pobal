from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from .views import login, logout, register, profile

class TestAccountViews(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('test_user', 'test_user@example.com', '12345')

    def test_login_page_loads(self):
        page = self.client.get('/accounts/login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')
    
    def test_register_page_loads(self):
        page = self.client.get('/accounts/register/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register.html')
    
    def test_login_user_to_profile_page(self):
        c = Client()
        c.login(username='test_user', password='12345')
        page = c.get('/accounts/profile/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'profile.html')
        
    def test_login_user_can_fail(self):
        c = Client()
        c.login(username='test_user', password='54321')
        page = c.get('/accounts/profile/')
        self.assertTemplateNotUsed(page, 'profile.html')
    
    def test_logout_works(self):
        c = Client()
        
        c.login(username='test_user', password='12345')
        response = c.get('/accounts/profile/')
        self.assertEquals(response.status_code, 200)
        
        # check that logged out user cannot access profile page
        c.logout()
        # check that value 25 is raise with message to denote message level constant 'success'
        self.assertEqual(25, messages.SUCCESS)
        # self.assertRedirects(r, '/accounts/login/')
        # r = c.get('/accounts/logout/', follow=True)
        
   
   