from django.contrib.auth.decorators import login_required
from django.template import Context
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsTaller import tallerForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.db import connection
from administracion.models import User, Empleado,Orden,JefeTaller,Venta,Cliente,Vendedor,RevisionVehiculo,Sucursal
from django.http import JsonResponse




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
    carros=RevisionVehiculo.objects.select_related('codigo_orden','codigo_venta')
    return render(request, 'taller/carrosTaller.html',{'carros':carros})
'''
@login_required
def busquedaCodigoVenta(request):
    if request.POST and 'btBuscar' in request.POST:

'''