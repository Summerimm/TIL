from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movie')

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()