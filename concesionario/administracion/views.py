from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404
from .formsAdministracion import UserForm, UserFormContrasena, UserFormEliminate, UserFormRecuperate, UserFormModificate, UserFormAux, EmpleadoFormAux
from .formsAdministracion import SucursalForm, FormSucursalModificar, VehiculoForm, FormVehiculoModificar
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.http import JsonResponse
from administracion.models import User, Cliente, JefeTaller, Vendedor, Gerente, Sucursal
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse


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
            tipo = user_form.cleaned_data['tipo']
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
            usuario.cedula = user_form.cleaned_data['cedula']
            usuario.direccion = user_form.cleaned_data['direccion']
            usuario.fecha_de_nacimiento = user_form.cleaned_data['fecha_de_nacimiento']
            usuario.telefono = user_form.cleaned_data['telefono']
            if "C" == tipo:
                UserForm.crearCliente(usuario)
            if "A" == tipo:
                usuario.is_superuser = True
                usuario.is_staff = True
                UserForm.crearAdministrador(usuario)
            if "V" == tipo:
                UserForm.crearVendedor(usuario)
            if "J" == tipo:
                UserForm.crearJefeTaller(usuario)
            if "G" == tipo:
                UserForm.crearGerente(usuario)
            messages.success(request,"El usuario "+usuario.username+" se ha creado satisfactoriamente")

        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        # formulario inicial
        user_form = UserForm()

    return render(request, 'administracion/crearUsuario.html', { 'user_form': user_form})  

@login_required
def modificarUsuario(request):
    if request.method == 'POST':
        user_form_aux = UserFormModificate(request.POST)
        
        if user_form_aux.is_valid():
            usernameChoice = user_form_aux.cleaned_data['usernameChoice']
            user = UserFormModificate.get(usernameChoice)
            if Cliente.objects.filter(id=user.id).count() > 0:
                return redirect('/administracion/modificarUsuarioCliente/' + str(user.id) +'/')
            elif Vendedor.objects.filter(id=user.id).count() > 0:
                return redirect('/administracion/modificarUsuarioVendedor/' + str(user.id) +'/')
            elif Gerente.objects.filter(id=user.id).count() > 0:
                return redirect('/administracion/modificarUsuarioGerente/' + str(user.id) +'/')
            elif JefeTaller.objects.filter(id=user.id).count() > 0:
                return redirect('/administracion/modificarUsuarioJefeTaller/' + str(user.id) +'/')
            else:
                return redirect('/administracion/modificarUsuarioAdministrador/' + str(user.id) +'/')
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        user_form_aux = UserFormModificate()

    return render(request, 'administracion/modificarUsuario.html', { 'user_form_aux': user_form_aux})

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
            messages.success(request,"El usuario "+username.username+" se ha eliminado satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

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
            messages.success(request,"El usuario "+username.username+" se ha recuperado satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        # formulario inicial
        user_form = UserFormRecuperate()

    return render(request, 'administracion/recuperarUsuario.html', { 'user_form': user_form})

@login_required
def modificarUsuarioAdministrador(request, idX):
    usernameText = UserFormModificate.getID(idX).username
    if request.method == 'POST':
        user_form = UserFormAux(request.POST)

        if user_form.is_valid():
            usuario = user_form
            usuario.first_name = user_form.cleaned_data['first_name']
            usuario.last_name = user_form.cleaned_data['last_name']
            usuario.email = user_form.cleaned_data['email']
            usuario.cedula = user_form.cleaned_data['cedula']
            usuario.direccion = user_form.cleaned_data['direccion']
            usuario.fecha_de_nacimiento = user_form.cleaned_data['fecha_de_nacimiento']
            usuario.telefono = user_form.cleaned_data['telefono']
            UserFormModificate.actualizarAdministrador(usuario, idX)
            messages.success(request,"El usuario "+usernameText+" se ha modificado satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        user = UserFormModificate.getID(idX)
        user_form = UserFormAux(instance=user)
    return render(request, 'administracion/modificarUsuarioAdministrador.html', {'user_form': user_form, 'usernameText': usernameText})

@login_required
def modificarUsuarioCliente(request, idX):
    usernameText = UserFormModificate.getID(idX).username
    if request.method == 'POST':
        user_form = UserFormAux(request.POST)

        if user_form.is_valid():
            usuario = user_form
            usuario.first_name = user_form.cleaned_data['first_name']
            usuario.last_name = user_form.cleaned_data['last_name']
            usuario.email = user_form.cleaned_data['email']
            usuario.cedula = user_form.cleaned_data['cedula']
            usuario.direccion = user_form.cleaned_data['direccion']
            usuario.fecha_de_nacimiento = user_form.cleaned_data['fecha_de_nacimiento']
            usuario.telefono = user_form.cleaned_data['telefono']
            UserFormModificate.actualizarAdministrador(usuario, idX)
            messages.success(request,"El usuario "+usernameText+" se ha modificado satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        user = UserFormModificate.getID(idX)
        user_form = UserFormAux(instance=user)
    return render(request, 'administracion/modificarUsuarioCliente.html', {'user_form': user_form, 'usernameText': usernameText})

@login_required
def modificarUsuarioVendedor(request, idX):
    userAux = UserFormModificate.getID(idX)
    usernameText = userAux.username
    vendedorAux = Vendedor.objects.get(id=userAux.id)
    sucursalActual = Sucursal.objects.get(codigo_sucursal=vendedorAux.codigo_sucursal_id).nombre
    if request.method == 'POST':
        user_form = EmpleadoFormAux(request.POST)

        if user_form.is_valid():
            sucursalChoice = user_form.cleaned_data['sucursalChoice']
            usuario = user_form
            usuario.first_name = user_form.cleaned_data['first_name']
            usuario.last_name = user_form.cleaned_data['last_name']
            usuario.email = user_form.cleaned_data['email']
            usuario.cedula = user_form.cleaned_data['cedula']
            usuario.sucursal = sucursalChoice.codigo_sucursal
            usuario.salario = user_form.cleaned_data['salario']
            usuario.direccion = user_form.cleaned_data['direccion']
            usuario.fecha_de_nacimiento = user_form.cleaned_data['fecha_de_nacimiento']
            usuario.telefono = user_form.cleaned_data['telefono']
            EmpleadoFormAux.actualizarVendedor(usuario, idX)
            messages.success(request,"El usuario "+usernameText+" se ha modificado satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        user = UserFormModificate.getID(idX)
        user_form = EmpleadoFormAux(instance=user, initial={"salario": vendedorAux.salario, 'sucursalChoice': vendedorAux.codigo_sucursal_id})
    return render(request, 'administracion/modificarUsuarioEmpleado.html', {'user_form': user_form, 'usernameText': usernameText, 'sucursalActual': sucursalActual})

@login_required
def modificarUsuarioGerente(request, idX):
    userAux = UserFormModificate.getID(idX)
    usernameText = userAux.username
    vendedorAux = Gerente.objects.get(id=userAux.id)
    sucursalActual = Sucursal.objects.get(codigo_sucursal=vendedorAux.codigo_sucursal_id).nombre
    if request.method == 'POST':
        user_form = EmpleadoFormAux(request.POST)

        if user_form.is_valid():
            sucursalChoice = user_form.cleaned_data['sucursalChoice']
            usuario = user_form
            usuario.first_name = user_form.cleaned_data['first_name']
            usuario.last_name = user_form.cleaned_data['last_name']
            usuario.email = user_form.cleaned_data['email']
            usuario.cedula = user_form.cleaned_data['cedula']
            usuario.sucursal = sucursalChoice.codigo_sucursal
            usuario.salario = user_form.cleaned_data['salario']
            usuario.direccion = user_form.cleaned_data['direccion']
            usuario.fecha_de_nacimiento = user_form.cleaned_data['fecha_de_nacimiento']
            usuario.telefono = user_form.cleaned_data['telefono']
            EmpleadoFormAux.actualizarGerente(usuario, idX)
            messages.success(request,"El usuario "+usernameText+" se ha modificado satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        user = UserFormModificate.getID(idX)
        user_form = EmpleadoFormAux(instance=user, initial={"salario": vendedorAux.salario, 'sucursalChoice': vendedorAux.codigo_sucursal_id})
    return render(request, 'administracion/modificarUsuarioEmpleado.html', {'user_form': user_form, 'usernameText': usernameText, 'sucursalActual': sucursalActual})

@login_required
def modificarUsuarioJefeTaller(request, idX):
    userAux = UserFormModificate.getID(idX)
    usernameText = userAux.username
    vendedorAux = JefeTaller.objects.get(id=userAux.id)
    sucursalActual = Sucursal.objects.get(codigo_sucursal=vendedorAux.codigo_sucursal_id).nombre
    if request.method == 'POST':
        user_form = EmpleadoFormAux(request.POST)

        if user_form.is_valid():
            sucursalChoice = user_form.cleaned_data['sucursalChoice']
            usuario = user_form
            usuario.first_name = user_form.cleaned_data['first_name']
            usuario.last_name = user_form.cleaned_data['last_name']
            usuario.email = user_form.cleaned_data['email']
            usuario.cedula = user_form.cleaned_data['cedula']
            usuario.sucursal = sucursalChoice.codigo_sucursal
            usuario.salario = user_form.cleaned_data['salario']
            usuario.direccion = user_form.cleaned_data['direccion']
            usuario.fecha_de_nacimiento = user_form.cleaned_data['fecha_de_nacimiento']
            usuario.telefono = user_form.cleaned_data['telefono']
            EmpleadoFormAux.actualizarJefeTaller(usuario, idX)
            messages.success(request,"El usuario "+usernameText+" se ha modificado satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        user = UserFormModificate.getID(idX)
        user_form = EmpleadoFormAux(instance=user, initial={"salario": vendedorAux.salario, 'sucursalChoice': vendedorAux.codigo_sucursal_id})
    return render(request, 'administracion/modificarUsuarioEmpleado.html', {'user_form': user_form, 'usernameText': usernameText, 'sucursalActual': sucursalActual})

@login_required
def modificarContrasena(request):
    if request.method == 'POST':

        # formulario enviado
        user_form = UserFormContrasena(request.POST)

        if user_form.is_valid():
            # formulario validado correctamente
            #usuario = user_form.save()
            username = user_form.cleaned_data['usernameChoice']
            password = user_form.cleaned_data['password']
            UserFormContrasena.modificar(username,make_password(password))
            messages.success(request,"La contrasena del usuario "+username.username+" se ha modificada satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        # formulario inicial
        user_form = UserFormContrasena()

    return render(request, 'administracion/modificarContrasena.html', { 'user_form': user_form})

@login_required
@csrf_exempt
def crearSucursal(request):
    if request.method == 'POST':

        # formulario enviado
        user_form = SucursalForm(request.POST)

        if user_form.is_valid():
            nombre = user_form.cleaned_data['nombre']
            direccion = user_form.cleaned_data['direccion']
            SucursalForm.guardarSucursal(nombre, direccion)
            messages.success(request,"La sucursal "+nombre+" se ha creado satisfactoriamente")

        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        # formulario inicial
        user_form = SucursalForm()

    return render(request, 'administracion/crearSucursal.html', { 'user_form': user_form})

@login_required
def modificarSucursalSeleccion(request):
    if request.method == 'POST':
        user_form_aux = FormSucursalModificar(request.POST)
        
        if user_form_aux.is_valid():
            sucursal = user_form_aux.cleaned_data['sucursalChoice']
            return redirect('/administracion/modificarSucursal/' + str(sucursal.codigo_sucursal) +'/')
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        user_form_aux = FormSucursalModificar()

    return render(request, 'administracion/modificarSucursalSeleccion.html', { 'user_form_aux': user_form_aux})

@login_required
def modificarSucursal(request, idX):
    sucursalAux = FormSucursalModificar.get(idX)
    usernameText = sucursalAux.nombre
    if request.method == 'POST':
        user_form = SucursalForm(request.POST)

        if user_form.is_valid():
            nombre = user_form.cleaned_data['nombre']
            direccion = user_form.cleaned_data['direccion']
            FormSucursalModificar.update(sucursalAux, nombre, direccion)
            messages.success(request,"La sucursal "+usernameText+" se ha modificado satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        user = FormSucursalModificar.get(idX)
        user_form = SucursalForm(instance=user)
    return render(request, 'administracion/modificarSucursal.html', {'user_form': user_form, 'usernameText': usernameText})

@login_required
def crearVehiculo(request):
    if request.method == 'POST':

        # formulario enviado
        user_form = VehiculoForm(request.POST)
        if user_form.is_valid():
            vehiculo = user_form
            vehiculo.marca = user_form.cleaned_data['marca']
            vehiculo.modelo = user_form.cleaned_data['modelo']
            vehiculo.descripcion = user_form.cleaned_data['descripcion']
            vehiculo.color = user_form.cleaned_data['color']
            vehiculo.cantidad = user_form.cleaned_data['cantidad']
            vehiculo.precio_unidad = user_form.cleaned_data['precio_unidad']
            VehiculoForm.guardar(vehiculo)
            messages.success(request,"El vehiculo "+vehiculo.modelo+" se ha creado satisfactoriamente")
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        # formulario inicial
        user_form = VehiculoForm()

    return render(request, 'administracion/crearVehiculo.html', {'user_form': user_form})
@login_required
def modificarVehiculo(request,idX):
    if request.method == 'POST':
        user_form = VehiculoForm(request.POST)
        if user_form.is_valid():
            vehiculo = user_form
            vehiculo.marca = user_form.cleaned_data['marca']
            vehiculo.modelo = user_form.cleaned_data['modelo']
            vehiculo.descripcion = user_form.cleaned_data['descripcion']
            vehiculo.color = user_form.cleaned_data['color']
            vehiculo.cantidad = user_form.cleaned_data['cantidad']
            vehiculo.precio_unidad = user_form.cleaned_data['precio_unidad']
            VehiculoForm.actualizar(vehiculo,idX)
            messages.success(request,"El vehiculo "+vehiculo.modelo+" se ha actualizado satisfactoriamente")
            usernameText = vehiculo.modelo + " - " + vehiculo.marca

    else:
        
        vehiculo = VehiculoForm.get(idX)
        user_form = VehiculoForm(instance=vehiculo)
        user_form.fields['color'] = VehiculoForm.setColor(vehiculo)
        user_form.fields['cantidad'] = VehiculoForm.setCantidad(vehiculo)
        user_form.fields['precio_unidad'] = VehiculoForm.setPrecio(vehiculo)
        usernameText = vehiculo.modelo + " - " + vehiculo.marca

    return render(request, 'administracion/modificarVehiculo.html', { 'user_form': user_form, 'usernameText': usernameText})

@login_required
def modificarVehiculoSeleccion(request):
    if request.method == 'POST':
        user_form_aux = FormVehiculoModificar(request.POST)
        
        if user_form_aux.is_valid():
            vehiculo = user_form_aux.cleaned_data['vehiculoChoice']
            return redirect('/administracion/modificarVehiculo/' + str(vehiculo.codigo_vehiculo) +'/')
        else:
            messages.warning(request, "No has diligenciado correctamente todos los campos")

    else:
        user_form_aux = FormVehiculoModificar()

    return render(request, 'administracion/modificarVehiculoSeleccion.html', { 'user_form_aux': user_form_aux})

def prueba(request):
	return JsonResponse({'foo':'bar'})