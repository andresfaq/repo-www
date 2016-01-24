from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsTaller import tallerForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from administracion.models import Orden,JefeTaller



@login_required
def inicio(request):
    return render(request, 'taller/index.html')

@login_required
def ingresarVehiculo(request):
        if request.POST:
            form = tallerForm(request.POST)
            if form.is_valid():
                #jefe=request.POST.get('selectJefeTaller', None)
                selectionJefe = form.cleaned_data['jefeTaller']
                estadoOr =  form.cleaned_data['estado']
                orden=Orden(codigo_jefe_taller=selectionJefe.codigo_jefe_taller,
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