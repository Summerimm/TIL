# my_project project -> urls.py
# my_project/my_project/urls.py

# from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]

