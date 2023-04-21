# Generated by Django 3.2.13 on 2023-04-21 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movie', to='movies.Actor'),
        ),
    ]