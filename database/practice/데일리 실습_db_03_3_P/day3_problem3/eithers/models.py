from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=100, verbose_name='RED TEAM')
    issue_b = models.CharField(max_length=100, verbose_name='BLUE TEAM')

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField(choices=[(True, 'RED TEAM'), (False, 'BLUE TEAM')], default='RED TEAM')
    content = models.CharField(max_length=100)