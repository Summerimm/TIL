from django.urls import path
from . import views

urlpatterns = [
    path('', views.fruit, name='fruit')
]
