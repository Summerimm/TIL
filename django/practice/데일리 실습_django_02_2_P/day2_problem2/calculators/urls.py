from django.urls import path
from . import views

urlpatterns = [
    path('calculator/<int:num1>/<int:num2>', views.calculate)
]
