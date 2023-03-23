from django.urls import path
from . import views

urlpatterns = [
    path('introduce/<str:name>/<int:age>', views.introduce)
]