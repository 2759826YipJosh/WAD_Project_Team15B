from django.db import models
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import csv
from django.core.management import BaseCommand
from django.db.models import Q
from django.shortcuts import render



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    NAME_MAX_LENGTH = 20
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Game(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateField()
    category = models.CharField(max_length=200)
    platforms_available = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1)
    age_restriction = models.IntegerField()
    multiplayer = models.BooleanField()
    average_completion_time = models.CharField(max_length=200)
    trailer_link = models.URLField()
    image_link = models.URLField()
    description = models.TextField()
    
    def __str__(self):
        return self.name