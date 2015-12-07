__author__ = 'andres'
from django.conf.urls import patterns, url
from administracion.views import inicio

urlpatterns = patterns('concesionario.administracion.views', url(r'^$', inicio))

