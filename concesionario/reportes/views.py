from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from administracion.models import User, Empleado, Vendedor, Venta, Vehiculo

@login_required
def inicio(request):
	return render(request, 'reportes/index.html')

@login_required
def usuarios(request):

	usuarios = User.objects.all()

	return render(request, 'reportes/usuarios.html', {'usuarios':usuarios})

@login_required
def inventario(request):
	return render(request, 'reportes/inventario.html')

@login_required
def ventas(request):

	vendedores = Vendedor.objects.all()
	ventas = Venta.objects.all()

	for vendedor in vendedores:

		#vendedor.num_ventas = len(vendedor.filter(codigo_vendedor=ventas.codigo_vendedor)
		vendedor.num_ventas = len(ventas.filter(codigo_vendedor=vendedor.codigo_vendedor))
		print(vendedor.first_name, vendedor.username, vendedor.num_ventas, vendedor.id_empleado, vendedor.codigo_vendedor)

	return render(request, 'reportes/ventas.html', {'vendedores':vendedores})