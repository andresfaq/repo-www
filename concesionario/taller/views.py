from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsTaller import tallerForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.db import connection
from administracion.models import User, Empleado,Orden,JefeTaller,Venta,Cliente,Vendedor
from django.http import JsonResponse




@login_required
def inicio(request):
    return render(request, 'taller/index.html')

@login_required
def ingresarVehiculo(request):
        if request.POST and 'submit' in request.POST:
            form = tallerForm(request.POST)
            if form.is_valid():
                #jefe=request.POST.get('selectJefeTaller', None)
                selectionJefe = form.cleaned_data['jefeTaller']
                #jefeT=form.jefeTaller._get_choices(selectionJefe)
                estadoOr =  form.cleaned_data['estado']
                orden=Orden(codigo_jefe_taller=selectionJefe,
                            diagnostico=form.clean_diagnostico(),
                            estado=estadoOr)
                orden.save()
                #render(request, 'taller/ingresarVehiculo.html', {'mensaje': "ENTRO EN EL IF"})
                return HttpResponseRedirect('/')

        else:
            form = tallerForm()
            #form.jefeTaller = JefeTaller.objects.all().order_by('first_name')
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

'''
@login_required
def busquedaCodigoVenta(request):
    if request.POST and 'btBuscar' in request.POST:

'''