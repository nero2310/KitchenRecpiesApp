from django.test import TestCase,Client,override_settings
from unittest.mock import patch
from .views import UserLogin

# Create your tests here.

class LoginTestCase(TestCase):
    def setUp(self):
        client = Client()

    @override_settings(POSTGRES_PASSWORD="example")
    def test_user_login(self):
        self.client.post(path="/auth/login")
