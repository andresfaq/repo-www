from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsTaller import tallerForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from administracion.models import User, Empleado, Orden,JefeTaller,Venta,Cliente
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
            print ("esta es la consulta: ",consulta)
            clientes = Cliente.objects.all()
            print ("lista de clientes: ",clientes)

            usuario = {'nombreCliente': 'Eduardo Ismael'}
            return JsonResponse(usuario)
        else:
            return HttpResponse('SOLO AJAX!')

    return HttpResponse()

'''
@login_required
def busquedaCodigoVenta(request):
    if request.POST and 'btBuscar' in request.POST:

'''