from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import (
    CommonPasswordValidator, MinimumLengthValidator, NumericPasswordValidator,
    UserAttributeSimilarityValidator, get_default_password_validators,
    get_password_validators, validate_password,
)
from django.core.exceptions import ValidationError
from .forms import UserLoginForm, UserRegistrationForm

class TestUserLoginForm(TestCase):
    def test_user_form_requires_two_fields(self):
        form = UserLoginForm({'username_or_email':'test_user'})
        self.assertFalse(form.is_valid())
        
    def test_user_form_can_take_email_and_password_combo(self):
        form = UserLoginForm({'username_or_email':'test_user@example.com', 'password':'12345'})
        self.assertTrue(form.is_valid())
    
    def test_user_login_takes_username_and_password_combo(self):
        form = UserLoginForm({'username_or_email':'test_user', 'password':'12345'})
        self.assertTrue(form.is_valid())

class TestPasswordValidation(TestCase):
    def test_get_default_password_validators(self):
        # check auth password validation settings in settings.py
        validators = get_default_password_validators()
        self.assertEqual(len(validators), 4)
        self.assertEqual(validators[0].__class__.__name__, 'UserAttributeSimilarityValidator')
        self.assertEqual(validators[1].__class__.__name__, 'MinimumLengthValidator')
        self.assertEqual(validators[2].__class__.__name__, 'CommonPasswordValidator')
        self.assertEqual(validators[3].__class__.__name__, 'NumericPasswordValidator')
        self.assertEqual(validators[1].min_length, 8)
    
    def test_password_of_less_than_8_characters_is_invalid(self):
        with self.assertRaises(ValidationError, args=['This password is too short.']) as error:
            validate_password('seven77')
        self.assertEqual(error.exception.messages, ['This password is too short. It must contain at least 8 characters.'])
    
    def test_password_validation_for_common_passwords(self):
        with self.assertRaises(ValidationError) as error:
            validate_password('password')
        self.assertEqual(error.exception.messages, ['This password is too common.'])

    def test_password_validation_for_numeric_string_is_false(self):
        with self.assertRaises(ValidationError) as error:
            validate_password('16722349')
        self.assertEqual(error.exception.messages, ["This password is entirely numeric."])
        
    def test_password_can_not_be_too_common_or_entirely_numeric(self):
        with self.assertRaises(ValidationError) as error:
            validate_password('12345678')
        self.assertEqual(error.exception.messages, ['This password is too common.', 'This password is entirely numeric.'])
        
class TestRegistrationForm(TestCase):
    def test_is_valid_with_four_fields(self):
        form = UserRegistrationForm({
            'username':'test_user',
            'email':'test_user@example.com',
            'password1':'12345',
            'password2':'12345'
        })
        self.assertTrue(form.is_valid())
        
    def test_NOT_valid_without_two_password_fields(self):
        form = UserRegistrationForm({
            'username':'test_user',
            'email':'test_user@example.com',
            'password2':'12345'
        })
        self.assertFalse(form.is_valid())
    
    def test_NOT_valid_with_different_passwords(self):
        form = UserRegistrationForm({
            'username':'test_user',
            'email':'test_user@example.com',
            'password1':'12345',
            'password2':'67987'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'password2': ['Passwords do not match']})
        
    def test_NOT_valid_with_existing_user(self):
         #create a new user
        User.objects.create_user(username='existing_user',
                                 email='user@example.com',
                                 password='user')
                                 
        # pass the new user' username the reg form
        form = UserRegistrationForm({
            'username':'existing_user',
            'email':'test_user@example.com',
            'password1':'12345',
            'password2':'12345'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'username': ['A user with that username already exists.']})
        
    def test_email_must_be_unique(self):
         #create a new user
        User.objects.create_user(username='existing_user',
                                 email='user@example.com',
                                 password='user')
                                 
        # pass the new user' username the reg form
        form = UserRegistrationForm({
            'username':'test_user',
            'email':'user@example.com',
            'password1':'12345',
            'password2':'12345'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'email': ['Email addresses must be unique.']})