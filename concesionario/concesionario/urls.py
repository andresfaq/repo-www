from django.conf.urls import include, url
from django.contrib import admin
from paginaweb.views import home, login, logout, loginMovil, estadoVehiculo, descripcion
admin.autodiscover() #registra todos los archivos admin.py del proyecto

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    url(r'^administracion/', include('administracion.urls')),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^reportes/', include('reportes.urls')),
    url(r'^ventas/', include('ventas.urls')),
    url(r'^taller/', include('taller.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^descripcion/$', descripcion, name='descripcion'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^loginMovil/$', loginMovil),
    url(r'^estadoVehiculo/$', estadoVehiculo),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
