import os
import re
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class CategoriesPageTests(TestCase):
    
    def test_categories_page_template(self):
        response = self.client.get(reverse('categories'))

        self.assertTemplateUsed(response, 'categories.html', f"{FAILURE_HEADER}HOMEPAGE NOT BEING USED{FAILURE_FOOTER}")
        

    def test_categories_images_load(self):
        response = self.client.get(reverse('categories'))
        
        image_urls = [
            '/static/images/COD.jpg',
            '/static/images/BF2024.jpg',
            '/static/images/halo.jpg',
            '/static/images/gta5v2.jpg',
            '/static/images/rd2.jpg',
            '/static/images/assassinscreed.jpg',
            '/static/images/EA.jpg',
            '/static/images/nba.jpg',
            '/static/images/f123.jpg',
        ]
        
        for image in image_urls:
            self.assertContains(response, image)


    def test_links_exists(self):
        response = self.client.get(reverse('categories'))
        
        game_urls = [
            '/search_results/?q=Call+Of+Duty+Modern+Warfare+3',
            '/search_results/?q=Battlefield+2042',
            '/search_results/?q=Halo+Infinite',
            '/search_results/?q=GTA+5',
            '/search_results/?q=Red+Dead+Redemption+2',
            "/search_results/?q=Assassin's+Creed+Odyssey",
            '/search_results/?q=EA+FC+24',
            '/search_results/?q=NBA+2k24',
            '/search_results/?q=F1+23',
        ]
        
        for game in game_urls:
            self.assertContains(response, game)