from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsTaller import tallerForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
'''from administracion import models.
'''


@login_required
def inicio(request):
    return render(request, 'taller/index.html')


def ingresarVehiculo(request):
        if request.POST:
            form = tallerForm(request.POST)
            if form.is_valid():
                form.save()

                return HttpResponseRedirect('/')
        else:
            form = tallerForm()
            #form.jefeTaller =

        args = {}
        args.update(csrf(request))

        args['form'] = form

        return render_to_response('taller/ingresarVehiculo.html',args,context_instance=RequestContext(request))