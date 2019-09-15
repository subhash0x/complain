from django.contrib import admin
from . import settings
from django.urls import include, path
from complain import urls
from django.views.generic.base import TemplateView
from deptadmin import urls
from assignee import urls
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('complain/', include(urls)),
    path('registration/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('deptadmin/', include(urls)),
    path('assignee/',include(urls)),

]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
