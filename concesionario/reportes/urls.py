from django.conf.urls import patterns, url, include
from reportes import views

urlpatterns = [
				url(r'^$', views.inicio),
				url(r'^usuarios$', views.usuarios)]


