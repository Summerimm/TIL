from django.urls import path
from . import views

urlpatterns = [
    path('<str:thing>/<int:cnt>', views.price),
]
