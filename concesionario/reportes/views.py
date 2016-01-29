from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from administracion import models


from rest_framework import generics


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

@login_required
def usuarios(request):

	usuarios = models.User.objects.all()

	return render(request, 'reportes/usuarios.html', {'usuarios':usuarios})

@login_required
def inventario(request):

	vehiculos = models.Vehiculo.objects.all()

	return render(request, 'reportes/inventario.html',{'vehiculos':vehiculos})

@login_required
def ventas(request):

	vendedores = models.Vendedor.objects.all()
	ventas = models.Venta.objects.all()

	for vendedor in vendedores:

		#vendedor.num_ventas = len(vendedor.filter(codigo_vendedor=ventas.codigo_vendedor)
		vendedor.num_ventas = len(ventas.filter(codigo_vendedor=vendedor.codigo_vendedor))

	return render(request, 'reportes/ventas.html', {'vendedores':vendedores})

@login_required
def repuesto(request):

	repuestos = models.Repuesto.objects.all()

	return render(request, 'reportes/repuesto.html',{'repuestos':repuestos})


class UserList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('User-list', request=request, format=format)
    })