# pages app -> urls.py
# my_project/pages/urls.py

# from django.urls import path
# from . import views

app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
