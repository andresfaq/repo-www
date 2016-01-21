from clientes import views
from django.conf.urls import url

urlpatterns = [url(r'^$', views.inicio),
               url(r'^reparaciones/$', views.reparaciones), ]