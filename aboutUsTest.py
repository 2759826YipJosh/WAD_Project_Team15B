import os
import re
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class AboutUsPageTests(TestCase):
    
    def test_about_page_template(self):
        response = self.client.get(reverse('about_us'))

        self.assertTemplateUsed(response, 'about_us.html', f"{FAILURE_HEADER}HOMEPAGE NOT BEING USED{FAILURE_FOOTER}")
        

    def test_about_us_images_load(self):
        response = self.client.get(reverse('about_us'))
        charlie_image = '/static/images/Charlie.jpg'
        krish_image = '/static/images/Krish.jpg'
        jiayu_image = '/static/images/Jiayu.jpg'
        josh_image = '/static/images/Josh.jpg'
        ryan_image = '/static/images/Ryan.jpg'
        
        self.assertContains(response, charlie_image)
        self.assertContains(response, krish_image)
        self.assertContains(response, jiayu_image)
        self.assertContains(response, josh_image)
        self.assertContains(response, ryan_image)
        
        
    def test_about_us_names_load(self):
        response = self.client.get(reverse('about_us'))
        charlie_name = '<p> Name: Charlie Lawson</p>'
        krish_name = '<p> Name: Krish Dokania</p>'
        jiayu_name = '<p> Name: Jiayu Li</p>'
        josh_name = '<p> Name: Josh Yip</p>'
        ryan_name = "<p> Name: Ryan O'Byrne</p>"
        
        self.assertContains(response, charlie_name)
        self.assertContains(response, krish_name)
        self.assertContains(response, jiayu_name)
        self.assertContains(response, josh_name)
        self.assertContains(response, ryan_name)