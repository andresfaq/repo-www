from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from administracion.models import User, Empleado, Vendedor, Venta, Vehiculo, Repuesto, Sucursal

@login_required
def inicio(request):

	sucursales = Sucursal.objects.all()
	vendedores = Vendedor.objects.all()
	ventas = Venta.objects.all()

	for vendedor in vendedores:

		#vendedor.num_ventas = len(vendedor.filter(codigo_vendedor=ventas.codigo_vendedor)
		vendedor.num_ventas = len(ventas.filter(codigo_vendedor=vendedor.codigo_vendedor))

	print(sucursales)
	for sucursal in sucursales:
		sucursal.num_ventas = 0
		for vendedor in vendedores:
			if vendedor.codigo_sucursal.codigo_sucursal == sucursal.codigo_sucursal:
				sucursal.num_ventas += vendedor.num_ventas 
				print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa: " + str(sucursal.num_ventas))

	return render(request, 'reportes/index.html',{'sucursales':sucursales})

@login_required
def usuarios(request):

	usuarios = User.objects.all()

	return render(request, 'reportes/usuarios.html', {'usuarios':usuarios})

@login_required
def inventario(request):

	vehiculos = Vehiculo.objects.all()

	return render(request, 'reportes/inventario.html',{'vehiculos':vehiculos})

@login_required
def ventas(request):

	vendedores = Vendedor.objects.all()
	ventas = Venta.objects.all()

	for vendedor in vendedores:

		#vendedor.num_ventas = len(vendedor.filter(codigo_vendedor=ventas.codigo_vendedor)
		vendedor.num_ventas = len(ventas.filter(codigo_vendedor=vendedor.codigo_vendedor))
		print(vendedor.first_name, vendedor.username, vendedor.num_ventas, vendedor.id_empleado, vendedor.codigo_vendedor)

	return render(request, 'reportes/ventas.html', {'vendedores':vendedores})

@login_required
def repuesto(request):

	repuestos = Repuesto.objects.all()

	return render(request, 'reportes/repuesto.html',{'repuestos':repuestos})