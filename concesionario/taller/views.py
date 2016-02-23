from django.contrib.auth.decorators import login_required
from django.template import Context
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsTaller import tallerForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.db import connection
from administracion.models import User, Empleado,Orden,JefeTaller,Venta,Cliente,Vendedor,RevisionVehiculo,Sucursal,InventarioRepuesto,RepuestosPorOrden,Repuesto
from django.http import JsonResponse
import json






@login_required
def inicio(request):
    return render(request, 'taller/index.html')

@login_required
def ingresarVehiculo(request):
        if request.POST and 'submit' in request.POST:
            form = tallerForm(request.POST,initial={'jefeTaller': request.session['nombre']})
            if form.is_valid():
                print(' codigo jefe ', request.session["codigo"],
                      ' nombre ', request.session["nombre"], 'apellido', request.session["apellido"],' cedula', request.session["cedula"])

                selectionJefe = JefeTaller.objects.get(codigo_jefe_taller=request.session["codigo"])
                diagnostico = form.cleaned_data['diagnostico']
                estadoOr =  form.cleaned_data['estado']
                sucursalJefe = Sucursal.objects.get(codigo_sucursal=request.session["codigoSucursal"])
                orden=Orden(codigo_jefe_taller=selectionJefe,diagnostico=diagnostico,estado=estadoOr,sucursal=sucursalJefe)
                orden.save()

                codigoOrden=Orden.objects.get(codigo_orden=orden.codigo_orden);
                codigoVenta= Venta.objects.get(codigo_venta=form.cleaned_data['codigoVenta'])
                fechaRevision= form.cleaned_data['fechaRevision']
                cambioAceite=form.cleaned_data['fechaCAceite']
                km=form.cleaned_data['kmVehiculo']

                revision= RevisionVehiculo(codigo_venta=codigoVenta,codigo_orden=codigoOrden,
                                           fecha_revision=fechaRevision,kilometraje=km,fecha_cambio_aceite=cambioAceite)
                revision.save()
                print("finalio correctamente")
                render(request, 'taller/ingresarVehiculo.html',Context({'mensaje': "La orden y la revision de vehiculo se han creado exitosamente"}))
                #return HttpResponseRedirect('/')

        else:
            sucursal=Sucursal.objects.get(codigo_sucursal=request.session["codigoSucursal"])
            form = tallerForm(initial={'jefeTaller': request.session['nombre']+" "+request.session["apellido"],'sucursal':sucursal.nombre})
            #render(request, 'taller/ingresarVehiculo.html', {'mensaje': "ENTRO EN EL ELSE"})
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render(request, 'taller/ingresarVehiculo.html',args)
        #return render_to_response('taller/ingresarVehiculo.html',args,context_instance=RequestContext(request))



#@csrf_exempt
@login_required
def busquedaCodigoVenta(request):
    if request.method == 'POST':        
        if request.is_ajax():
            consulta = request.POST.get('nombreCliente')
            print ("esta es la consulta: ", consulta)
            clientes = Cliente.objects.filter(first_name__icontains=consulta)
            ventas = Venta.objects.all()

            listaCliente=[]
            for c in clientes:
                for v in ventas:
                    if(c.codigo_cliente == v.codigo_cliente.codigo_cliente):
                        #listaCliente.append([c.first_name,c.last_name,v.codigo_venta])
                        listaCliente.append([{'nombreCliente':c.first_name},
                                            {'apellidoCliente':c.last_name},
                                            {'codigoVenta':v.codigo_venta}])

            if(len(listaCliente)):
                for l in listaCliente:
                    print ("algo")
                    print ("nombre: ", l[0], " apellido :", l[1]," codigo vena: ",l[2])
            else:
                print("no hay datos que mostrar")


            #usuario = {'nombreCliente': 'Eduardo Ismael'}
            #datos = {'contenido': listaCliente}
            return JsonResponse(listaCliente,safe=False)
        else:
            return HttpResponse('SOLO AJAX!')

    return HttpResponse()


@login_required
def mostrarVehiculosTaller(request):
    form = tallerForm(request.POST)
    carros=RevisionVehiculo.objects.select_related('codigo_orden','codigo_venta')
    repuestos=InventarioRepuesto.objects.select_related('codigo_repuesto')#tengo que cambiar, no se debe cargar aquí
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['carros']=carros
    args['repuestos']=repuestos
    return render(request, 'taller/carrosTaller.html',args)

@login_required
def agregarRepuestosVehiculo(request):
    print(" llego al view ")
    if request.method == 'POST':
        if request.is_ajax():
            codigoOrden = request.POST.get('codigo_Orden')
            repuestosArray =request.POST.getlist('repuestos_array[]')

            print ("esta es la consulta: ", codigoOrden,"  el array rep: ",repuestosArray)
            for repuesto in repuestosArray:
               infoRepuesto=[int(x) for x in repuesto.split(',')]
               print("repuesto: ",infoRepuesto[0]," cantidad : ", infoRepuesto[1])

               orden = Orden.objects.get(codigo_orden=codigoOrden)
               repuestoAdd= Repuesto.objects.get(codigo_repuesto=infoRepuesto[0])
               repuesto_Orden=RepuestosPorOrden(codigo_orden=orden,
                                                codigo_repuesto=repuestoAdd,
                                                cantidad=infoRepuesto[1])
               invRepuesto = InventarioRepuesto.objects.get(codigo_repuesto=repuestoAdd)
               invRepuesto.cantidad = invRepuesto.cantidad - infoRepuesto[1]
               repuesto_Orden.save()
               invRepuesto.save()

            algo={'mensaje':"Proceso realizado"}
            return JsonResponse(algo,safe=False)
    return HttpResponse()

@login_required
def verOrdenVehiculo(request):
    print("llego a ver orden")
    if request.method == 'POST':
        if request.is_ajax():
            codigoOrden = request.POST.get('codigo_Orden')
            codigoRevision = request.POST.get('codigo_Revision')
            orden = Orden.objects.select_related('codigo_jefe_taller').get(codigo_orden=codigoOrden)
            repOrden = RepuestosPorOrden.objects.select_related('codigo_orden','codigo_repuesto').filter(codigo_orden=codigoOrden)
            arrayR = []

            for rep in repOrden:
                repuesto = {}
                repuesto['repuestoN']= rep.codigo_repuesto.nombre
                repuesto['repuestoDes']= rep.codigo_repuesto.descripcion
                repuesto['cantidadD']= rep.cantidad
                arrayR.append(repuesto)

            revisionV = RevisionVehiculo.objects.get(codigo_revision=codigoRevision)
            contenido={'sucursal': str(orden.sucursal),
                       'diagnostico': str(orden.diagnostico),
                       'jefeTF': str(orden.codigo_jefe_taller.first_name),
                       'jefeTL': str(orden.codigo_jefe_taller.last_name),
                       'fechaCA': str(revisionV.fecha_cambio_aceite),
                       'listaRep': arrayR}

            return JsonResponse(contenido,safe=False)
    return HttpResponse()


@login_required
def agregarRefaccion(request):
    if request.method == 'POST':
        print("hola entro en el post")
        nombre = request.POST.get('inpNombre')
        descripcion = request.POST.get('inpDescripcion')
        cantidad = request.POST.get('inpCantidad')
        precio = request.POST.get('inpPrecio')

        if((nombre != "") and (descripcion != "") and (cantidad != "") and (precio != "")):
            print("entro en el if")
            nuevoRepuesto = Repuesto(nombre=nombre,descripcion=descripcion)
            nuevoRepuesto.save()
            nuevoInventario = InventarioRepuesto(codigo_repuesto=nuevoRepuesto,
                                                 cantidad=cantidad,precio_unidad=precio)
            nuevoInventario.save()
            args = {}
            args.update(csrf(request))
            args['mensajeRep'] = 'Repuesto registrado exitosamente'
            args['inpNombre'] =""
            args['inpDescripcion'] =""
            args['inpCantidad'] = 0
            args['inpPrecio'] = 0
            return render(request, 'taller/agregarRepuesto.html',args)

        else:
            args = {}
            args.update(csrf(request))
            args['mensajeRep'] = 'Error al registrar Repuesto, verifique informacion'
            return render(request, 'taller/agregarRepuesto.html',args)


    else:
       return render(request, 'taller/agregarRepuesto.html')


@login_required
def verRepuestos(request):
    print("llego a repuestos")
    repuestosInfo = InventarioRepuesto.objects.select_related('codigo_repuesto')
    args = {}
    args.update(csrf(request))
    args['repuestos']= repuestosInfo
    return render(request,'taller/repuestos.html',args)

def modificarRepuesto(request):
    if request.method == 'POST':
        if request.is_ajax():
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            cantidad = request.POST.get('cantidad')
            precio = request.POST.get('precio')
            codigo = request.POST.get('codigo')
            print("datos",nombre,codigo)
            repuesto = Repuesto.objects.get(codigo_repuesto=codigo)
            repuesto.nombre = nombre
            repuesto.descripcion = descripcion
            repuesto.save()

            inventarioR = InventarioRepuesto.objects.get(codigo_repuesto=repuesto)
            inventarioR.cantidad = cantidad
            inventarioR.precio_unidad = precio
            inventarioR.save()

            contenido={'c':True}
            return JsonResponse(contenido,safe=False)

    return render(request,'taller/repuestos.html')

'''
@login_required
def busquedaCodigoVenta(request):
    if request.POST and 'btBuscar' in request.POST:

'''