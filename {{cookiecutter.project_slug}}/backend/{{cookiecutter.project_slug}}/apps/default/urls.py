# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views import generic

urlpatterns = [
    url(r'^about/$', generic.TemplateView.as_view(template_name='default/about.html'),
        name='about'),
    url(r'^$', generic.TemplateView.as_view(template_name='default/home.html'),
        name='home'),
]