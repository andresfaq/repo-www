from django.conf.urls import include, url
from django.contrib import admin
from paginaweb.views import home, login, logout,concesionario
admin.autodiscover() #registra todos los archivos admin.py del proyecto



urlpatterns = [
    url(r'^administracion/', include('administracion.urls')),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^reportes/', include('reportes.urls')),
    url(r'^ventas/', include('ventas.urls')),
    url(r'^taller/', include('taller.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^autos/$', concesionario, name='concesionario'),

]
