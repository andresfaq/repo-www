from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def inicio(request):
    return render(request, 'clientes/index.html')


@login_required
def reparaciones(request):
    return render(request, 'clientes/reparaciones.html.html')
