from django.conf.urls import patterns, url, include
from administracion.views import inicio

from tastypie.api import Api
from administracion.api import UserResource, OrdenResource, DatosVehiculoResource, GerenteResource, JefeTallerResource, VendedorResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(DatosVehiculoResource())
v1_api.register(OrdenResource())
v1_api.register(GerenteResource())
v1_api.register(JefeTallerResource())
v1_api.register(VendedorResource())

urlpatterns = patterns('concesionario.administracion.views',
                       url(r'^$', inicio), url(r'^api/',
                       include(v1_api.urls)))


