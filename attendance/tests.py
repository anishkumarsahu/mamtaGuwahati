from django.test import TestCase

# Create your tests here.
from .models import *

from django.test import TestCase
from .models import LoginSystem
from django.contrib.auth.models import User


class LoginSystemTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_system = LoginSystem.objects.create(
            systemName='Test System',
            location='Test Location',
            username='testuser',
            password='testpassword',
            userID=self.user,
            isDeleted=False,
        )

    def test_login_system_creation(self):
        self.assertEqual(self.login_system.systemName, 'Test System')
        self.assertEqual(self.login_system.location, 'Test Location')
        self.assertEqual(self.login_system.username, 'testuser')
        self.assertEqual(self.login_system.password, 'testpassword')
        self.assertEqual(self.login_system.userID, self.user)
        self.assertFalse(self.login_system.isDeleted)

    def test_login_system_str_representation(self):
        self.assertEqual(str(self.login_system), 'Test System')