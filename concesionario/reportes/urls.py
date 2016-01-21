from django.conf.urls import patterns, url, include
from reportes import views

urlpatterns = [url(r'^$', views.inicio),
			   url(r'^usuarios$', views.usuarios),
			   url(r'^inventario$', views.inventario),
			   url(r'^ventas$', views.ventas),
			   url(r'^repuesto$', views.repuesto),]




