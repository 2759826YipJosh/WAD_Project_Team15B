# Generated by Django 4.2.11 on 2024-03-08 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameDB', '0002_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameTitle', models.CharField(max_length=60)),
                ('releaseDate', models.DateField()),
                ('platform', models.CharField(max_length=20)),
                ('developer', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
                ('avgRating', models.FloatField()),
                ('ageRating', models.CharField(max_length=4)),
                ('multiplayer', models.BooleanField()),
                ('avgCompTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('ratingNum', models.IntegerField()),
                ('reviewText', models.CharField(max_length=1000)),
            ],
        ),
    ]