from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as log, logout as lout
from administracion.views import inicio as index_administracion
from ventas.views import inicio as index_ventas
from clientes.views import inicio as index_clientes
from taller.views import inicio as index_taller
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from administracion import models
from administracion.models import User, Empleado,Orden,JefeTaller,Sucursal

def es_gerente(user):
    return user.groups.filter(name='Gerentes').exists()

def es_vendedor(user):
    return user.groups.filter(name='Vendedores').exists()

def es_jefetaller(user):
    return user.groups.filter(name='JefesTaller').exists()

def es_cliente(user):
    return user.groups.filter(name='Clientes').exists()

def descripcion(request):
    return render(request, 'paginaweb/descripcion.html')

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

                jefe=JefeTaller.objects.get(username=user)
                sucur=jefe.codigo_sucursal

                request.session["codigoSucursal"] = sucur.getCodigoS()
                request.session["codigo"] = jefe.codigo_jefe_taller
                request.session["nombre"] = jefe.first_name
                request.session["apellido"] = jefe.last_name
                request.session["cedula"] = jefe.cedula
                return redirect(index_taller) #taller/index.html
            else:
                return redirect(home)

        else:
            return redirect(home)

    else:
        return render(request, 'registration/login.html')


def logout(request):
    lout(request)
    return render(request, 'registration/logout.html')


# def concesionario(request):
#     return render(request, 'paginaweb/contenidoAutos.html')

# def taller(request):
#     return render(request, 'paginaweb/contenidoReparacion.html')

@csrf_exempt
def loginMovil(request):
    try:
        print(request)
        dic = json.loads(request.body.decode('utf-8'))
        user = dic['username']
        passwd = dic['password']
        auth = authenticate(username=user, password=passwd)

    except Exception as e:
        print(e)
        return JsonResponse({'auth':"False"})

    if auth is not None:
        return JsonResponse({'auth':"True"})
    else:
        return JsonResponse({'auth':"False"})

@csrf_exempt
def estadoVehiculo(request):

    try:

        clientes = models.Cliente.objects.all()
        ordenes = models.Orden.objects.all()
        ventas = models.Venta.objects.all()

        peticion = json.loads(request.body.decode('utf-8'))
        codigo_orden = peticion['codigo_orden']
        placa = peticion['placa']

        venta_placa = ventas.filter(placa=placa).get()

        estado_orden = ordenes.filter(codigo_orden=codigo_orden).get()

        if(venta_placa.placa == placa or str(estado_orden.codigo_orden) == str(codigo_orden)):
            print(estado_orden.codigo_orden == codigo_orden)
            print(str(estado_orden.codigo_orden), str(codigo_orden))
            print('entre')

        return JsonResponse({'estado':estado_orden.estado})

    except Exception as e:
        print(e)

        return JsonResponse({'estado':"Sin estado, consulte sus compras"})







