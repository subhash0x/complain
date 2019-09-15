from django.contrib import admin
from django.urls import include, path
from complain import urls
from django.views.generic.base import TemplateView
from deptadmin import urls
from assignee import urls
from accounts import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('complain/', include(urls)),
    path('registration/', include('django.contrib.auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('deptadmin/', include(urls)),
    path('assignee/',include(urls)),
    path('accounts/',include(urls)),

]
