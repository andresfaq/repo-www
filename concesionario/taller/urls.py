from django.conf.urls import patterns, url, include
from taller import views


urlpatterns = [url(r'^$', views.inicio, name='inicio_taller'),
               url(r'^ingresarVehiculo/$', views.ingresarVehiculo, name='ingresarVehiculo'),
               url(r'^busquedaCodigoVenta/$', views.busquedaCodigoVenta, name='busquedaCodigoVenta'),
               url(r'^carrosTaller/$', views.mostrarVehiculosTaller, name='mostrarVehiculosTaller'),
               url(r'^carrosTaller/agregarRepuestosVehiculo/$', views.agregarRepuestosVehiculo, name='agregarRepuestosVehiculo'),
               url(r'^carrosTaller/verOrdenVehiculo/$', views.verOrdenVehiculo, name='verOrdenVehiculo'),
               url(r'^agregarRefaccion/$', views.agregarRefaccion, name='agregarRefaccion'),
               url(r'^repuestos/$', views.verRepuestos, name='verRepuestos'),
               url(r'^repuestos/modificar/$', views.modificarRepuesto, name='modificarRepuesto'), ]

# urlpatterns = patterns('concesionario.taller.views',
#                        url(r'^$', views.inicio),
#                        url(r'^ingresarVehiculo/$', views.ingresarVehiculo, name='ingresarVehiculo')
#                        )
