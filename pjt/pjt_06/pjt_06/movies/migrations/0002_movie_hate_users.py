# Generated by Django 3.2.13 on 2023-04-14 03:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='hate_users',
            field=models.ManyToManyField(related_name='hate_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
