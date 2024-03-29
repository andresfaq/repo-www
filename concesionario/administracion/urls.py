from django.conf.urls import patterns, url, include
from administracion.views import inicio
from administracion.views import crearUsuario
from administracion.views import modificarUsuario
from administracion.views import eliminarUsuario
from administracion.views import recuperarUsuario
from administracion.views import modificarUsuarioAdministrador
from administracion.views import modificarUsuarioCliente
from administracion.views import modificarUsuarioVendedor
from administracion.views import modificarUsuarioGerente
from administracion.views import modificarUsuarioJefeTaller
from administracion.views import modificarContrasena
from administracion.views import crearSucursal
from administracion.views import modificarSucursal
from administracion.views import modificarSucursalSeleccion
from administracion.views import crearVehiculo
from administracion.views import modificarVehiculo
from administracion.views import modificarVehiculoSeleccion
from administracion.views import prueba

from tastypie.api import Api
from administracion.api import UserResource, OrdenResource, DatosVehiculoResource, GerenteResource, JefeTallerResource, VendedorResource, DatosOrdenMovilResource, ClienteResource, DatosVentasClienteResource, DatosRevisionesVehiculoResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(DatosVehiculoResource())
v1_api.register(OrdenResource())
v1_api.register(GerenteResource())
v1_api.register(JefeTallerResource())
v1_api.register(VendedorResource())
v1_api.register(DatosOrdenMovilResource())
v1_api.register(ClienteResource())
v1_api.register(DatosVentasClienteResource())
v1_api.register(DatosRevisionesVehiculoResource())

urlpatterns = [url(r'^$', inicio),
			   url(r'^api/', include(v1_api.urls)),
               url(r'^crearUsuario/$', crearUsuario, name='crearUsuario'),
			   url(r'^modificarUsuario/$', modificarUsuario, name='modificarUsuario'),
			   url(r'^modificarUsuarioAdministrador/(?P<idX>\d+)/$', modificarUsuarioAdministrador, name='modificarUsuarioAdministrador'),
			   url(r'^modificarUsuarioCliente/(?P<idX>\d+)/$', modificarUsuarioCliente, name='modificarUsuarioCliente'),
			   url(r'^modificarUsuarioVendedor/(?P<idX>\d+)/$', modificarUsuarioVendedor, name='modificarUsuarioVendedor'),
			   url(r'^modificarUsuarioGerente/(?P<idX>\d+)/$', modificarUsuarioGerente, name='modificarUsuarioGerente'),
			   url(r'^modificarUsuarioJefeTaller/(?P<idX>\d+)/$', modificarUsuarioJefeTaller, name='modificarUsuarioJefeTaller'),
			   url(r'^modificarContrasena/$', modificarContrasena, name='modificarContrasena'),
			   url(r'^eliminarUsuario/$', eliminarUsuario, name='eliminarUsuario'),
			   url(r'^recuperarUsuario/$', recuperarUsuario, name='recuperarUsuario'),
			   url(r'^crearSucursal/$', crearSucursal, name='crearSucursal'),
			   url(r'^modificarSucursal/(?P<idX>\d+)/$', modificarSucursal, name='modificarSucursal'),
			   url(r'^modificarSucursalSeleccion/$', modificarSucursalSeleccion, name='modificarSucursalSeleccion'),
			   url(r'^crearVehiculo/$', crearVehiculo, name='crearVehiculo'),
			   url(r'^modificarVehiculo/(?P<idX>\d+)/$', modificarVehiculo, name='modificarVehiculo'),
			   url(r'^modificarVehiculoSeleccion/$', modificarVehiculoSeleccion, name='modificarVehiculoSeleccion'),
			   url(r'^prueba/$', prueba, name='prueba'),
			   ]