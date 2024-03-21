import os
import re
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class LoginPageTests(TestCase):
    
    def test_login_page_template(self):
        response = self.client.get(reverse('login'))

        self.assertTemplateUsed(response, 'login.html', f"{FAILURE_HEADER}HOMEPAGE NOT BEING USED{FAILURE_FOOTER}")
        

    def test_login_works(self):
        
        self.user = User.objects.create_user(username='testUser', email='test@example.com', password='testPassword')
        response = self.client.post(reverse('login'), {'username': 'testUser', 'password': 'testPassword'})
        self.assertRedirects(response, '/account/')
        
        
        
        