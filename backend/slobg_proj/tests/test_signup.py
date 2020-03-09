from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from slobg_app.forms import SignUpForm

class MyTests(TestCase):
    def test_forms(self):
        print("Running Signup Test...")
        form_data = {
            'username' : "testUsername",
            'first_name' : "testFirstName", 
            'last_name' : "testLastName", 
            'email' : "testEmail@email.com", 
            'password1' : "testPassword", 
            'password2' : "testPassword"
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

class LogInTest(TestCase):
    def setUp(self):
        print("Running Login Test...")
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
