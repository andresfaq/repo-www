from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .formsTaller import tallerForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


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

        args = {}
        args.update(csrf(request))

        args['form'] = form

        return render('taller/index.html',args)