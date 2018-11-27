from django.test import TestCase
from django.contrib.auth.password_validation import (
    CommonPasswordValidator, MinimumLengthValidator, NumericPasswordValidator,
    UserAttributeSimilarityValidator, get_default_password_validators,
    get_password_validators, validate_password,
)
from django.core.exceptions import ValidationError
from .forms import UserLoginForm, UserRegistrationForm

class TestUserLoginForm(TestCase):
    def test_user_form_requires_two_fields(self):
        form = UserLoginForm({'username_or_email':'test_user', 'password':'12345'})
        self.assertTrue(form.is_valid())
        
    def test_user_form_can_take_email_and_password_combo(self):
        form = UserLoginForm({'username_or_email':'test_user@example.com', 'password':'12345'})
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
