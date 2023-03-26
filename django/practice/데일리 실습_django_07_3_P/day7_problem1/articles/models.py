from django.db import models
# from imagekit.models import ImageSpecField
# from imagekit.processors import Thumbnail
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    # image_thumbnail = models.ImageSpecField