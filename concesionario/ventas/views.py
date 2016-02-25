from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .formsVentas import VehiculoFormAll, VehiculoFormOne, ClienteForm, UserForm
from administracion.models import Vehiculo
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.hashers import make_password


# Create your views here.
@login_required
def inicio(request):
	return render(request, 'ventas/index.html')

@login_required
def listarCarros(request):
	carros = VehiculoFormAll.vehiculos
	user_form = VehiculoFormAll(request.POST)
	if request.method == 'POST':
		if user_form.is_valid():
			marca = user_form.cleaned_data['marcaChoice']
			precio = user_form.cleaned_data['precioChoice']
			carros = VehiculoFormAll.vehiculosFiltro(marca,precio)
	else:
		user_form = VehiculoFormAll()

	return render(request, 'ventas/listarCarros.html', { 'user_form': user_form, 'carros': carros})

@login_required
def comprarCarro(request, codigo_vehiculo):
	if request.method == "POST":
		user_form = ClienteForm(request.POST)
		vehiculo = VehiculoFormOne.get(codigo_vehiculo)
		if user_form.is_valid():
			
			username = user_form.cleaned_data['clienteChoice']

			session = Session.objects.get(session_key=request.session.session_key)
			uid = session.get_decoded().get('_auth_user_id')
			user = User.objects.get(pk=uid)

			placa = ClienteForm.generarPlaca()
			porcentaje_descuento = user_form.cleaned_data['porcentaje_descuento']

			vendido = VehiculoFormOne.save(vehiculo.codigo_vehiculo, username, user, placa, porcentaje_descuento)
			if vendido:
				messages.success(request, "El "+vehiculo.marca+" del modelo "+vehiculo.modelo+ " con placas "+placa+" ha sido vendido exitosamente a "+username.username+" por "+user.username+"!")
			else:
				messages.warning(request, "Usted no es un vendedor, por lo tanto no puede vender")
		else:
			messages.warning(request, "No has diligenciado correctamente todos los campos")
	else:
		vehiculo = VehiculoFormOne.get(codigo_vehiculo)
		vehiculo.valor = VehiculoFormAll.soloCosto(vehiculo)
		user_form = ClienteForm()
	return render(request, 'ventas/comprarCarro.html', { 'user_form': user_form, 'vehiculo': vehiculo})

@login_required
def cotizarCarros(request):
	carros = VehiculoFormAll.vehiculos
	user_form = VehiculoFormAll(request.POST)
	if request.method == 'POST':
		if user_form.is_valid():
			marca = user_form.cleaned_data['marcaChoice']
			precio = user_form.cleaned_data['precioChoice']
			carros = VehiculoFormAll.vehiculosFiltro(marca,precio)
	else:
		user_form = VehiculoFormAll()

	return render(request, 'ventas/cotizarCarros.html', { 'user_form': user_form, 'carros': carros})

@login_required
def cotizarCarro(request,codigo_vehiculo):
	vehiculo = VehiculoFormOne.get(codigo_vehiculo)
	cartX =VehiculoFormOne.marcar(vehiculo)
	if cartX != 0:
		messages.warning(request, "El "+vehiculo.marca+" del modelo "+vehiculo.modelo+ " ya había sido cotizado")
	else:
		messages.success(request, "El "+vehiculo.marca+" del modelo "+vehiculo.modelo+ " ha sido agregado a la cotizacion")

	carros = VehiculoFormAll.vehiculos
	user_form = VehiculoFormAll(request.POST)
	if request.method == 'POST':
		if user_form.is_valid():
			marca = user_form.cleaned_data['marcaChoice']
			precio = user_form.cleaned_data['precioChoice']
			carros = VehiculoFormAll.vehiculosFiltro(marca,precio)
	else:
		user_form = VehiculoFormAll()

	return render(request, 'ventas/cotizarCarros.html', { 'user_form': user_form, 'carros': carros})

@login_required
def cotizacion(request):
	vehiculos = VehiculoFormAll.vehiculoCompleto(VehiculoFormOne.cotizados())
	costo = VehiculoFormOne.costoCotizados(vehiculos)
	user_form = ClienteForm(request.POST)
	if request.method == 'POST' and "vender" in request.POST:

		if user_form.is_valid():

			username = user_form.cleaned_data['clienteChoice']
			session = Session.objects.get(session_key=request.session.session_key)
			uid = session.get_decoded().get('_auth_user_id')
			user = User.objects.get(pk=uid)
			i = 0
			vendido = True
			for vehiculo in vehiculos:
				placa = ClienteForm.generarPlaca()
				porcentaje_descuento = user_form.cleaned_data['porcentaje_descuento']
				vendido = VehiculoFormOne.save(vehiculo.codigo_vehiculo, username, user, placa, porcentaje_descuento)
				i=i+1
			if i==0:
				messages.warning(request, "No hay carros en la cotizacion")
			elif vendido:
				VehiculoFormOne.borrarCotizados(vehiculos)
				messages.success(request, "Todos los vehiculos han sido vendidos a "+str(username.username)+" por un valor total de $"+str(costo))
			else:
				messages.warning(request, "Usted no es un vendedor, por lo tanto no puede vender")
		else:
			messages.warning(request, "No has diligenciado correctamente todos los campos")
	elif request.method == 'POST' and "eliminar" in request.POST:
		VehiculoFormOne.borrarCotizados(vehiculos)
		messages.success(request, "Los vehiculos de la cotizacion han sido eliminados")
	else:
		user_form = ClienteForm()
	return render(request, 'ventas/cotizacion.html', {'user_form': user_form, 'vehiculos': vehiculos, 'costo': costo})

@login_required
@csrf_exempt
def cliente(request):
    if request.method == 'POST':

        # formulario enviado
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            usuario = user_form
            usuario.password = make_password(user_form.cleaned_data['password'])
            usuario.is_superuser = False
            usuario.username = user_form.cleaned_data['username']
            usuario.first_name = user_form.cleaned_data['first_name']
            usuario.last_name = user_form.cleaned_data['last_name']
            usuario.email = user_form.cleaned_data['email']
            usuario.is_staff = False
            usuario.is_active = True
            usuario.cedula = user_form.cleaned_data['cedula']
            usuario.direccion = user_form.cleaned_data['direccion']
            usuario.fecha_de_nacimiento = user_form.cleaned_data['fecha_de_nacimiento']
            usuario.telefono = user_form.cleaned_data['telefono']
            UserForm.crearCliente(usuario)

            messages.success(request,"El usuario "+usuario.username+" se ha creado satisfactoriamente")

        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos o el cliente ya existe")

    else:
        # formulario inicial
        user_form = UserForm()

    return render(request, 'ventas/crearCliente.html', { 'user_form': user_form})  