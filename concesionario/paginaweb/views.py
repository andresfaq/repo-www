from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as log, logout as lout
from administracion.views import inicio


def home(request):
    return render(request, 'paginaweb/index.html')


def login(request):
    # user = request.POST['username']
    # passwd = request.POST['password']
    user = request.POST.get('username')
    passwd = request.POST.get('password')
    user = authenticate(username=user, password=passwd)
    if user is not None:
        if user.is_active:

            log(request, user)
            return redirect(inicio) #administracion/index.html
        else:
            return redirect(home) #paginaweb/index.html

    else:
        return render(request, 'registration/login.html')


def logout(request):
    lout(request)
    return render(request, 'registration/logout.html')

def concesionario(request):
    return  render (request, 'paginaweb/contenidoAutos.html')
