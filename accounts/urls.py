from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
