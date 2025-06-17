from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProductForm, ContactForm
from decimal import Decimal

class UserRegistrationFormTest(TestCase):
    def test_valid_registration_form(self):
        form_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        form_data = {
            'username': 'newuser',
            'email': 'invalid-email',
            'password1': 'testpass123',
            'password2': 'differentpass'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertIn('password2', form.errors)

class ProductFormTest(TestCase):
    def test_valid_product_form(self):
        form_data = {
            'name': 'Test Product',
            'brand': 'Test Brand',
            'price': '99.99',
            'description': 'Test Description',
            'image': 'https://example.com/image.jpg',
            'rating': '4.5',
            'quantity': '10',
            'stock': '10'
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_product_form(self):
        form_data = {
            'name': '',  # Required field
            'brand': 'Test Brand',
            'price': 'invalid',  # Invalid price
            'description': 'Test Description',
            'image': 'not-a-url',  # Invalid URL
            'stock': 'invalid'  # Invalid stock
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('price', form.errors)
        self.assertIn('image', form.errors)
        self.assertIn('rating', form.errors)
        self.assertIn('stock', form.errors)

class ContactFormTest(TestCase):
    def test_valid_contact_form(self):
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'consult': '1',  # Reclamo
            'message': 'Test message',
            'notices': True
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        form_data = {
            'name': '',  # Required field
            'email': 'invalid-email',  # Invalid email
            'consult': '999',  # Invalid consult type
            'message': '',  # Required field
            'notices': True
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('consult', form.errors)
        self.assertIn('message', form.errors) 