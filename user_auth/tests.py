from django.test import TestCase,Client,override_settings,RequestFactory
from django.contrib import auth
from django.contrib.auth.models import User

from os import environ

from .views import UserLogin

# Create your tests here.


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="Jhon",password="very_hard_password")

    @override_settings(POSTGRES_PASSWORD=environ["POSTGRES_PASSWORD"])
    def test_user_login(self):
        request = self.client.post(path="/auth/login")
        request.user = self.user
        view = UserLogin()
        view.setup(request)
        assert self.client.session['_auth_user_id']
        
