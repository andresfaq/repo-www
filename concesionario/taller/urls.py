from django.conf.urls import patterns, url, include
from taller import views


urlpatterns = [url(r'^$', views.inicio, name='inicio_taller'),
               url(r'^ingresarVehiculo/$', views.ingresarVehiculo, name='ingresarVehiculo'),
               url(r'^busquedaCodigoVenta/$', views.busquedaCodigoVenta, name='busquedaCodigoVenta'),
               url(r'^carrosTaller/$', views.mostrarVehiculosTaller, name='mostrarVehiculosTaller'), ]

# urlpatterns = patterns('concesionario.taller.views',
#                        url(r'^$', views.inicio),
#                        url(r'^ingresarVehiculo/$', views.ingresarVehiculo, name='ingresarVehiculo')
#                        )
