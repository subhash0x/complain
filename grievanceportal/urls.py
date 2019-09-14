from django.contrib import admin
from django.urls import include, path
from complain import urls
<<<<<<< HEAD
from django.views.generic.base import TemplateView
=======
from deptadmin import urls
from assignee import urls
>>>>>>> 6843cfde658b61783b3cd14b96b4e270a6f88b45

urlpatterns = [
    path('admin/', admin.site.urls),
    path('complain/', include(urls)),
    path('registration/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('deptadmin/', include(urls)),
    path('assignee/',include(urls)),

]
