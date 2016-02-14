from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .formsVentas import VehiculoFormAll, VehiculoFormOne, ClienteForm
from administracion.models import Vehiculo
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib import messages

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

			VehiculoFormOne.save(vehiculo.codigo_vehiculo, username, user)
			messages.success(request, "El "+vehiculo.marca+" del modelo "+vehiculo.modelo+" ha sido vendido exitosamente a "+username.username+" por "+user.username+"!")
	else:
		vehiculo = VehiculoFormOne.get(codigo_vehiculo)
		user_form = ClienteForm()
	return render(request, 'ventas/comprarCarro.html', { 'user_form': user_form, 'vehiculo': vehiculo})