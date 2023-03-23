from django.db import models

class Article(model.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()