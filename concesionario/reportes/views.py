from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from administracion import models
from rest_framework import generics
from reportes.serializers import UserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import user_passes_test

def es_gerente(user):
    return user.groups.filter(name='Gerentes').exists()






@user_passes_test(es_gerente, login_url='/login/')
@login_required
def inicio(request):

	sucursales = models.Sucursal.objects.all()
	vendedores = models.Vendedor.objects.all()
	ventas = models.Venta.objects.all()

	for vendedor in vendedores:

		vendedor.num_ventas = len(ventas.filter(codigo_vendedor=vendedor.codigo_vendedor))

	print(sucursales)
	for sucursal in sucursales:
		sucursal.num_ventas = 0
		for vendedor in vendedores:
			if vendedor.codigo_sucursal.codigo_sucursal == sucursal.codigo_sucursal:
				sucursal.num_ventas += vendedor.num_ventas 

	return render(request, 'reportes/index.html',{'sucursales':sucursales})

@user_passes_test(es_gerente, login_url='/login/')
@login_required
def usuarios(request):

	usuarios = models.User.objects.all()

	return render(request, 'reportes/usuarios.html', {'usuarios':usuarios})

@user_passes_test(es_gerente, login_url='/login/')
@login_required
def inventario(request):

	vehiculos = models.Vehiculo.objects.all()

	return render(request, 'reportes/inventario.html',{'vehiculos':vehiculos})

@user_passes_test(es_gerente, login_url='/login/')
@login_required
def ventas(request):

	vendedores = models.Vendedor.objects.all()
	ventas = models.Venta.objects.all()

	for vendedor in vendedores:

		#vendedor.num_ventas = len(vendedor.filter(codigo_vendedor=ventas.codigo_vendedor)
		vendedor.num_ventas = len(ventas.filter(codigo_vendedor=vendedor.codigo_vendedor))

	return render(request, 'reportes/ventas.html', {'vendedores':vendedores})


@user_passes_test(es_gerente, login_url='/login/')
@login_required
def reparaciones(request):

	jefes_taller = models.JefeTaller.objects.all()
	sucursales = models.Sucursal.objects.all()
	ordenes = models.Orden.objects.all()

	for jefetaller in jefes_taller:
		jefetaller.num_ordenes = len(ordenes.filter(codigo_jefe_taller=jefetaller.codigo_jefe_taller))

	print(sucursales)
	for sucursal in sucursales:
		sucursal.num_ordenes = 0
		for jefetaller in jefes_taller:
			if jefetaller.codigo_sucursal.codigo_sucursal == sucursal.codigo_sucursal:
				sucursal.num_ordenes += jefetaller.num_ordenes 

	print(sucursales)

	return(render(request, 'reportes/reparaciones.html', {'sucursales':sucursales}))


@user_passes_test(es_gerente, login_url='/login/')
@login_required
def ordenes(request):

	revisiones = models.RevisionVehiculo.objects.all()
	revision1 = revisiones.filter(codigo_orden__sucursal__codigo_sucursal=1).order_by('fecha_revision')
	revision2 = revisiones.filter(codigo_orden__sucursal__codigo_sucursal=2).order_by('fecha_revision')
	revision3 = revisiones.filter(codigo_orden__sucursal__codigo_sucursal=3).order_by('fecha_revision')

	fechas1 = {}

	for revision in revision1:

		if not revision.fecha_revision in fechas1:

			revision.num_ordenes = revision1.filter(fecha_revision=revision.fecha_revision).count()
			fechas1[revision.fecha_revision]=revision.num_ordenes
			print(revision.num_ordenes)

	revision1 = revision1.distinct('fecha_revision')

	fechas2 = {}

	for revision in revision2:

		if not revision.fecha_revision in fechas2:
			revision.num_ordenes = revision2.filter(fecha_revision=revision.fecha_revision).count()
			fechas2[revision.fecha_revision]=revision.num_ordenes

	revision2 = revision2.distinct('fecha_revision')

	fechas3 = {}

	for revision in revision3:

		if not revision.fecha_revision in fechas3:
			revision.num_ordenes = revision3.filter(fecha_revision=revision.fecha_revision).count()
			fechas3[revision.fecha_revision]=revision.num_ordenes

	revision3 = revision3.distinct('fecha_revision')

	return render(request,'reportes/ordenes.html',{'revision1':revision1,'revision2':revision2 ,'revision3':revision3,'fechas1':fechas1,'fechas2':fechas2,'fechas3':fechas3})


@user_passes_test(es_gerente, login_url='/login/')
@login_required
def repuesto(request):
	repuestos = models.Repuesto.objects.all()
	return render(request, 'reportes/repuesto.html',{'repuestos':repuestos})


class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)