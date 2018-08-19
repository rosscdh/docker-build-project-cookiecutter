# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

admin.site.site_header = '{{ cookiecutter.project_name }} - Administration'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^health/', include('health_check.urls')),
    url(r'^api/v1/', include(('tester.apps.api.urls', 'api_v1'), namespace='api_v1')),
    url(r'^', include(('{{ cookiecutter.project_slug }}.apps.default.urls', 'default'), namespace='default')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)