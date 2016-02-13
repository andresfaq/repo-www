from django.conf.urls import patterns, url, include
from administracion.views import inicio
from administracion.views import crearUsuario
from administracion.views import modificarUsuario
from administracion.views import eliminarUsuario
from administracion.views import recuperarUsuario

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
			   url(r'^eliminarUsuario/$', eliminarUsuario, name='eliminarUsuario'),
			   url(r'^recuperarUsuario/$', recuperarUsuario, name='recuperarUsuario'),
			   ]