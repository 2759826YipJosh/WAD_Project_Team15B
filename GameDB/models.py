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
    
    gameTitle = models.CharField(max_length=60)
    releaseDate = models.DateField()
    #Don't edit these foreign keys once active will break admin page - Ryan
    #categoryName = models.ForeignKey(Category, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20)
    developer = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    avgRating = models.FloatField()
    ageRating = models.CharField(max_length=4)
    multiplayer = models.BooleanField()
    avgCompTime = models.TimeField()
    videoName = models.CharField(max_length=30, null=True, blank=True, unique=True)
    pictureName = models.CharField(max_length=30, null=True, blank=True, unique=True)
    description = models.CharField(max_length=1000, null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.gameTitle

class Review(models.Model):

    title = models.CharField(max_length=30)
    ratingNum = models.IntegerField()
    reviewText = models.CharField(max_length=1000)
    #Don't edit these foreign keys once active will break admin page - Ryan
    #username = models.ForeignKey(User.username)
    #gameTitle = models.ForeignKey(Game.gameTitle)
    #gameID = models.ForeignKey(Game.gameID)
    
    def __str__(self):
        return self.title
    
class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            for row in reader:
                game = Game.objects.create(
                    gameTitle=row[0],
                    releaseDate=row[1],
                    platform=row[2],
                    developer=row[3],
                    publisher=row[4],
                    avgRating=float(row[5]),
                    ageRating=row[6],
                    multiplayer=bool(row[7]),
                    avgCompTime=row[8],
                    videoName=row[9],
                    pictureName=row[10],
                    description=row[11]
                )
                
def search(request):
    query = request.GET.get('q')
    if query:
        results = Game.objects.filter(
            Q(gameTitle__icontains=query) |
            Q(platform__icontains=query) |
            Q(developer__icontains=query) |
            Q(publisher__icontains=query)
        )
    else:
        results = Game.objects.none()

    return render(request, 'chosen_game.html', {'results': results})