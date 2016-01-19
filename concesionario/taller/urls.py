from django.conf.urls import patterns, url, include
from concesionario.taller import views

urlpatterns = patterns('concesionario.taller.views',
                       url(r'^$', views.inicio),
                       url(r'^ingresarVehiculo/$', views.ingresarVehiculo, name='ingresarVehiculo')
                       )
