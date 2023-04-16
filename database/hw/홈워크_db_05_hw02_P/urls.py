# accounts/urls.py

from django.urls import path
app_name = 'accounts'
urlpatterns = [
    ...
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]