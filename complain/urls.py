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
    # path('complaintform/',complaintform),
    # path('registration/', include('django.contrib.auth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
<<<<<<< HEAD
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
=======
    path('complaintform', TemplateView.as_view(template_name='complain/complaintform.html'), name='complaintform'),
>>>>>>> 5fc984d1ee7454adb5bd35733cb71907a8c74d72
    # url('admin/', admin.site.urls),

]
