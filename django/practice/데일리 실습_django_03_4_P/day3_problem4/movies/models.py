from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=10)
    director = models.CharField(default='Unknown', max_length=20)

    def __str__(self) -> str:
        return f"{self.pk}번째 영화 - {self.title} : ({self.genre})"