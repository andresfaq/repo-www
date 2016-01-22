from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as log, logout as lout
from administracion.views import inicio as index_administracion
from ventas.views import inicio as index_ventas
from clientes.views import inicio as index_clientes
from taller.views import inicio as index_taller


def es_gerente(user):
    return user.groups.filter(name='Gerentes').exists()

def es_vendedor(user):
    return user.groups.filter(name='Vendedores').exists()

def es_jefetaller(user):
    return user.groups.filter(name='JefesTaller').exists()

def es_cliente(user):
    return user.groups.filter(name='Clientes').exists()



def home(request):
    return render(request, 'paginaweb/index.html')


def login(request):
    user = request.POST.get('username')
    passwd = request.POST.get('password')
    user = authenticate(username=user, password=passwd)

    if user is not None:

        if user.is_active:
            log(request, user)

            if es_gerente(user):
                return redirect(index_administracion) #administracion/index.html

            if es_vendedor(user):
                return redirect(index_ventas) #ventas/index.html

            if es_cliente(user):
                return redirect(index_clientes) #clientes/index.html

            if es_jefetaller(user):
                return redirect(index_taller) #clientes/index.html
            else:
                return redirect(home)

        else:
            return redirect(home) #paginaweb/index.html

    else:
        return render(request, 'registration/login.html')


def logout(request):
    lout(request)
    return render(request, 'registration/logout.html')


# def concesionario(request):
#     return render(request, 'paginaweb/contenidoAutos.html')

# def taller(request):
#     return render(request, 'paginaweb/contenidoReparacion.html')




