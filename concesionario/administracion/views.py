from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsAdministracion import UserForm, UserFormEliminate, UserFormRecuperate, UserFormModificateAux
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
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            # formulario validado correctamente
            usuario = user_form
            usuario.id = UserForm.identificacion() + 1
            usuario.password = make_password(user_form.cleaned_data['password'])
            usuario.is_superuser = False
            usuario.username = user_form.cleaned_data['username']
            usuario.first_name = user_form.cleaned_data['first_name']
            usuario.last_name = user_form.cleaned_data['last_name']
            usuario.email = user_form.cleaned_data['email']
            usuario.is_staff = False
            usuario.is_active = True
            usuario.date_joined = '2000-10-10' #Poner la fecha del dia actual
            usuario.cedula = user_form.cleaned_data['cedula']
            usuario.direccion = user_form.cleaned_data['direccion']
            usuario.fecha_de_nacimiento = user_form.cleaned_data['fecha_de_nacimiento']
            usuario.telefono = user_form.cleaned_data['telefono']
            usuario.save()
            
        else:
            print("asd")

    else:
        # formulario inicial
        user_form = UserForm()

    return render(request, 'administracion/crearUsuario.html', { 'user_form': user_form})  

@login_required
def modificarUsuario(request):
    if request.method == 'POST':
        user_form_aux = UserFormModificateAux(request.POST)
        user_form = UserForm(request.POST)
        complete = False
        user = ""
        if user != "":
            user_form = UserForm(instance=user)
        
        if user_form_aux.is_valid():
            usernameChoice = user_form_aux.cleaned_data['usernameChoice']
            user = UserFormModificateAux.get(usernameChoice)
            complete = True

        if user != "":
            user_form = UserForm(instance=user)

        else:
            print("asd")

        if user_form.is_valid():
            usuario = user_form
            usuario.password = user_form.cleaned_data['password']
            usuario.username = user_form.cleaned_data['username']
            usuario.first_name = user_form.cleaned_data['first_name']
            usuario.last_name = user_form.cleaned_data['last_name']
            usuario.email = user_form.cleaned_data['email']
            usuario.cedula = user_form.cleaned_data['cedula']
            usuario.direccion = user_form.cleaned_data['direccion']
            usuario.fecha_de_nacimiento = user_form.cleaned_data['fecha_de_nacimiento']
            usuario.telefono = user_form.cleaned_data['telefono']
            usuario.save()
            

        else:
            print("asdas")


    else:
        # formulario inicial
        user_form_aux = UserFormModificateAux()
        user_form = UserForm(request.POST)

    return render(request, 'administracion/modificarUsuario.html', { 'user_form_aux': user_form_aux, 'user_form': user_form})
    #return render(request, 'administracion/modificarUsuario.html', )

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
            print("asd")

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