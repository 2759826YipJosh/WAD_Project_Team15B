# Generated by Django 4.2.11 on 2024-03-08 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GameDB', '0005_alter_game_gameid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
    ]
