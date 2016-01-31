from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsAdministracion import UserForm, UserFormEliminate, UserFormRecuperate
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.http import JsonResponse
from administracion.models import User, Cliente
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.hashers import make_password


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
            usuario = user_form.save()
            usuario.id = UserForm.identificacion()
            truePass = make_password(usuario.password)
            usuario.password = truePass
            usuario.is_superuser = True
            usuario.is_staff = True
            usuario.is_active = True
            usuario.date_joined = '2000-10-10'
            #usuario.fecha_de_nacimiento = '2000-10-10'
            #usuario.save()
            return HttpResponseRedirect('/great/'+truePass)
        else:
            print("asd")

    else:
        # formulario inicial
        user_form = UserForm(instance=request.user)

    return render(request, 'administracion/crearUsuario.html', { 'user_form': user_form})  

@login_required
def modificarUsuario(request):
    return render(request, 'administracion/modificarUsuario.html')

@login_required
def eliminarUsuario(request):
    if request.method == 'POST':

        # formulario enviado
        user_form = UserFormEliminate(request.POST)

        if user_form.is_valid():
            # formulario validado correctamente
            #usuario = user_form.save()
            username = user_form.cleaned_data['usernameChoice']
            UserFormEliminate.eliminate(username)
        else:
            return HttpResponseRedirect('/AquiDeberíaDeHaberUnMensajeDeError/')

    else:
        # formulario inicial
        user_form = UserFormEliminate()

    return render(request, 'administracion/eliminarUsuario.html', { 'user_form': user_form})

@login_required
def recuperarUsuario(request):
    if request.method == 'POST':

        # formulario enviado
        user_form = UserFormRecuperate(request.POST)

        if user_form.is_valid():
            # formulario validado correctamente
            #usuario = user_form.save()
            username = user_form.cleaned_data['usernameChoice']
            UserFormRecuperate.recuperate(username)
        else:
            return HttpResponseRedirect('/AquiDeberíaDeHaberUnMensajeDeError/')

    else:
        # formulario inicial
        user_form = UserFormRecuperate()

    return render(request, 'administracion/recuperarUsuario.html', { 'user_form': user_form}) 