import os
import re
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class ComingSoonPageTests(TestCase):
    
    def test_coming_soon_page_template(self):
        response = self.client.get(reverse('coming_soon'))

        self.assertTemplateUsed(response, 'coming_soon.html', f"{FAILURE_HEADER}HOMEPAGE NOT BEING USED{FAILURE_FOOTER}")
        

    def test_coming_soon_images_load(self):
        response = self.client.get(reverse('coming_soon'))
        
        image_urls = [
            '/static/images/gta6.jpg',
            '/static/images/F1.jpg',
            '/static/images/starwars.jpg',
        ]
        
        for image in image_urls:
            self.assertContains(response, image)


    def test_links_exists(self):
        response = self.client.get(reverse('coming_soon'))
        
        youtube_urls = [
            'https://youtu.be/QdBZY2fkU-0?si=3xeMsQbVlj5yHTSL',
            'https://youtu.be/4rCs87muGjc?si=8Q4bv5ZO1aCH9-rn',
            'https://youtu.be/ymcpwq1ltQc?si=2gMg4NVDvOIRzod8',
        ]
        
        for url in youtube_urls:
            self.assertContains(response, url)