from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def inicio(request):
    return render(request, 'administracion/index.html')

@login_required
def crearUsuario(request):
	return render(request, 'administracion/index.html')

@login_required
def modificarUsuario(request):
	return render(request, 'administracion/index.html')

@login_required
def eliminarUsuario(request):
	return render(request, 'administracion/index.html')