from django.conf.urls import patterns, url, include
from ventas.views import inicio
from ventas.views import listarCarros, comprarCarro, cotizarCarros, cotizarCarro, cotizacion, cliente



urlpatterns = [url(r'^$', inicio),
			   url(r'^listarCarros$', listarCarros, name='listarCarros'),
			   url(r'^comprarCarro/(?P<codigo_vehiculo>\d+)/$', comprarCarro, name='comprarCarro'),
			   url(r'^cotizarCarros$', cotizarCarros, name='cotizarCarros'),
			   url(r'^cotizarCarro/(?P<codigo_vehiculo>\d+)/$', cotizarCarro, name='cotizarCarro'),
			   url(r'^cotizacion$', cotizacion, name='cotizacion'),
			   url(r'^cliente$', cliente, name='cliente'),
			   ]

#Static en vez de media