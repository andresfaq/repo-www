from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from reportes import views

urlpatterns = [url(r'^$', views.inicio,name="reporte_inicio"),
				url(r'^usuarios$', views.usuarios),
				url(r'^inventario$', views.inventario),
				url(r'^ventas$', views.ventas),
				url(r'^repuesto$', views.repuesto),
				url(r'^reparaciones$', views.reparaciones),
				url(r'^ordenes$', views.ordenes),
				url(r'^user/$', views.UserList.as_view()),
				url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
				]

urlpatterns = format_suffix_patterns(urlpatterns)




