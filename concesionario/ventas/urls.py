from django.conf.urls import patterns, url, include
from ventas.views import inicio
from ventas.views import listarCarros, comprarCarro



urlpatterns = [url(r'^$', inicio),
			   url(r'^listarCarros$', listarCarros, name='listarCarros'),
			   url(r'^comprarCarro/(?P<codigo_vehiculo>\d+)/$', comprarCarro, name='comprarCarro'),

			   ]

#Static en vez de media
#Porcentaje de descuento
#Sucursal para gerente
#Placa