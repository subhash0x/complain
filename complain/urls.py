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
    path('test/', home),
    # path('registration/', include('django.contrib.auth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # url('admin/', admin.site.urls),

]