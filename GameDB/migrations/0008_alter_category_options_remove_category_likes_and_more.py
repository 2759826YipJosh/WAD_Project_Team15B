# Generated by Django 4.2.11 on 2024-03-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameDB', '0007_category_likes_category_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='game',
            name='pictureName',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='game',
            name='videoName',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
