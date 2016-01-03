from django.conf.urls import patterns, url, include
from administracion.views import inicio

from tastypie.api import Api
from administracion.api import UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())

urlpatterns = patterns('concesionario.administracion.views',
                       url(r'^$', inicio), url(r'^api/',
                       include(v1_api.urls)))


