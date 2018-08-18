# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

admin.site.site_header = '{{ cookiecutter.project_name }} - Administration'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^health/', include('health_check.urls')),
    url(r'^', include(('{{ cookiecutter.project_slug }}.apps.public.urls', 'public'), namespace='public')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)