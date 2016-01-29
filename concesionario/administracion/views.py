from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsAdministracion import UserForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.http import JsonResponse
from administracion.models import User
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@login_required
def inicio(request):
    return render(request, 'administracion/index.html')

@login_required
@csrf_exempt
def crearUsuario(request):
    if request.method == 'POST':

        # formulario enviado
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            # formulario validado correctamente
            usuario = user_form.save(commit=False)
            usuario.is_superuser = False
            usuario.is_staff = False
            usuario.is_active = False
            usuario.fecha_de_nacimiento = '2000-10-10'
            usuario.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/falla/')

    else:
        # formulario inicial
        user_form = UserForm(instance=request.user)

    #return render_to_response('administracion/crearUsuario.html', { 'user_form': user_form}, context_instance=RequestContext(request))
    return render(request, 'administracion/crearUsuario.html', { 'user_form': user_form})  

@login_required
def modificarUsuario(request):
    return render(request, 'administracion/modificarUsuario.html')

@login_required
def eliminarUsuario(request):
    return render(request, 'administracion/eliminarUsuario.html')