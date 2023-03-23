# articles app -> urls.py
# my_project/articles/urls.py

# from django.urls import path
# from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
]