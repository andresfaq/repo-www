from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsAdministracion import crearUsuarioForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.http import JsonResponse
from administracion.models import Cliente

@login_required
def inicio(request):
    return render(request, 'administracion/index.html')

@login_required
def crearUsuario(request):
    if request.POST and 'submit' in request.POST:
        form = crearUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['nombreUsuario']
            contrasenaUsuario = form.cleaned_data['contrasenaUsuario']
            tipoUsuario = form.cleaned_data['tipoUsuario']
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            cedula = form.cleaned_data['cedula']
            email = form.cleaned_data['email']
            fecha = form.cleaned_data['fecha']
            telefono = form.cleaned_data['telefono']
            return HttpResponseRedirect('/')
    else:
        form = crearUsuarioForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'administracion/crearUsuario.html',args)

@login_required
def modificarUsuario(request):
	return render(request, 'administracion/modificarUsuario.html')

@login_required
def eliminarUsuario(request):
	return render(request, 'administracion/eliminarUsuario.html')