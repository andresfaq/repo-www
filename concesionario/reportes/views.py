from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def inicio(request):
    return render(request, 'reportes/index.html')

@login_required
def usuarios(request):
    return render(request, 'reportes/usuarios.html')


