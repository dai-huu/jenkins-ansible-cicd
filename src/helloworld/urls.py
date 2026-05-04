"""helloworld URL Configuration"""
from django.urls import path
from app import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
