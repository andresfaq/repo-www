from django.conf.urls import patterns, url, include
from ventas.views import inicio



urlpatterns = patterns('concesionario.ventas.views',
                       url(r'^$', inicio))



"""=======
from tastypie.api import Api
from reportes.api import UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())

urlpatterns = [
				url(r'^$', views.inicio),
				url(r'^usuarios$', views.usuarios),
				url(r'^inventario$', views.inventario),
				url(r'^ventas$', views.ventas),
				url(r'^api/', include(v1_api.urls))]
>>>>>>> 672eb5a7d9d2c6e96f940680de2d2a62095e2181"""