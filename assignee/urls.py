from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import path, include
from .views import *
from complain import urls
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

urlpatterns = [
    path('assigntest/', assignpersonhome),
    path('admin/', admin.site.urls),


]
