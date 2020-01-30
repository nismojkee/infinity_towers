from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apartments', views.apartments, name='apartments'),
    path('gallery', views.gallery, name='gallery'),
    path('location', views.location, name='location'),
    path('level', views.level, name='level'),
    path('room', views.room, name='room'),
]
