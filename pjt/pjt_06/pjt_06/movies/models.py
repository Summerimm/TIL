from django.db import models
from django.conf import settings

class Movie(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_movies')
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'영화 제목: {self.title}'
    
class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'댓글 내용: {self.content}, 작성자ID: {self.user_id} 영화ID: {self.movie_id}'
