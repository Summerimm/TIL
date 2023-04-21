from django.urls import path, include
from . import views

app_name = "movies"

urlpatterns = [
    path("actors/", views.actor_index),
    path("actors/<int:actor_pk>/", views.actor_detail),
    path("movies/", views.movie_index),
    path("movies/<int:movie_pk>/", views.movie_detail),
    path("reviews/", views.review_index),
    path("reviews/<int:review_pk>/", views.review_detail),
]
