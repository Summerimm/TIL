from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
