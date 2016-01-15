from django.conf.urls import patterns, url, include
from ventas.views import inicio



urlpatterns = patterns('concesionario.ventas.views',
                       url(r'^$', inicio))




