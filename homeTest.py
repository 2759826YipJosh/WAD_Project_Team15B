import os
import re
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"



class HomePageTests(TestCase):
    

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html', f"{FAILURE_HEADER}HOMEPAGE NOT BEING USED{FAILURE_FOOTER}")

    def test_home_page_contains_carousel(self):
        response = self.client.get('/')
        self.assertContains(response, '<div id="main_carousel" class="carousel slide" data-bs-ride="carousel">')



    
    def test_carousel_prev_button_exists(self):
        response = self.client.get('/')
        self.assertContains(response, '<button class="carousel-control-prev" type="button" data-bs-target="#main_carousel" data-bs-slide="prev">')
        
    
                    
    
    def test_carousel_prev_button_exists(self):
        response = self.client.get('/')
        self.assertContains(response, '<button class="carousel-control-next" type="button" data-bs-target="#main_carousel" data-bs-slide="next">')
        
        
        
    def test_home_page_carousel_contains_image(self):
        response = self.client.get('/')

        banner_image = '/static/images/gameDBbanner.jpg'
        reviews_image = '/static/images/gamereviews.jpg'
        gta_5_image = '/static/images/gta5.jpg'
        
        self.assertContains(response, banner_image)
        self.assertContains(response, reviews_image)
        self.assertContains(response, gta_5_image)




    def test_home_page_contains_popular_categories_link(self):
        response = self.client.get('/')
        self.assertContains(response, '<a href="categories/" class="text-white btn btn-dark btn-lg">Popular Categories</a>')
        
    
    def test_home_page_contains_coming_soon_link(self):
        response = self.client.get('/')
        self.assertContains(response, '<a href="comingsoon/" class="text-white btn btn-dark btn-lg">Coming Soon</a>')


    def test_home_page_contains_images(self):
        response = self.client.get('/')
        
        fps_image = '/static/images/FPS.jpg'
        rpg_image = '/static/images/RPG.jpg'
        sport_image = '/static/images/sport.jpg'
        gta6_image = '/static/images/gta6.jpg'
        f1_image = '/static/images/F1.jpg'
        star_wars_image = '/static/images/starwars.jpg'

                
        self.assertContains(response, fps_image)
        self.assertContains(response, rpg_image)
        self.assertContains(response, sport_image)
        self.assertContains(response, gta6_image)
        self.assertContains(response, f1_image)
        self.assertContains(response, star_wars_image)


