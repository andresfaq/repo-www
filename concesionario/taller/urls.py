from django.conf.urls import patterns, url, include
from taller import views



urlpatterns = patterns('concesionario.taller.views',
                       url(r'^$', views.inicio),
                       url(r'^ingresarCarro/$', views.ingresarVehiculo, name='ingresarCarroTaller')
                       )
