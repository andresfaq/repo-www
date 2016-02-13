from django import forms
from paginaweb.static import *
import datetime
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from administracion.models import User, JefeTaller, Vendedor, Gerente, Cliente, Empleado, Sucursal

class UserForm(forms.ModelForm):

    CHOICES = (('A','Administrador'),( 'G','Gerente'),('J','Jefe de taller'),('V','Vendedor'),('C','Cliente'))
    tipo = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'cedula',
            'direccion',
            'fecha_de_nacimiento',
            'telefono'
            )

    def identificacion():
        numID = User.objects.count()
        return numID

    def tipoUsuario(tipo):
        if tipo=="C":
            numID = Cliente.objects.count() + 1
            return numID

        elif tipo=="V":
            numID = Vendedor.objects.count() + 1
            return numID
        elif tipo=="G":
            print("G")
        elif tipo=="J":
            print("J")
        elif tipo=="A":
            print("A")

    def crearAdministrador(usuario):
        User.objects.create(username=usuario.username,password=usuario.password,is_superuser=usuario.is_superuser,first_name=usuario.first_name,last_name=usuario.last_name,email=usuario.email,is_staff=usuario.is_staff,is_active=usuario.is_active,cedula=usuario.cedula,direccion=usuario.direccion,fecha_de_nacimiento=usuario.fecha_de_nacimiento,telefono=usuario.telefono)

    def crearCliente(usuario):
        Cliente.objects.create(username=usuario.username,password=usuario.password,is_superuser=usuario.is_superuser,first_name=usuario.first_name,last_name=usuario.last_name,email=usuario.email,is_staff=usuario.is_staff,is_active=usuario.is_active,cedula=usuario.cedula,direccion=usuario.direccion,fecha_de_nacimiento=usuario.fecha_de_nacimiento,telefono=usuario.telefono)

    def crearVendedor(usuario):
        Vendedor.objects.create(username=usuario.username,password=usuario.password,is_superuser=usuario.is_superuser,first_name=usuario.first_name,last_name=usuario.last_name,email=usuario.email,is_staff=usuario.is_staff,is_active=usuario.is_active,cedula=usuario.cedula,direccion=usuario.direccion,fecha_de_nacimiento=usuario.fecha_de_nacimiento,telefono=usuario.telefono,porcentaje_comision=0,salario=0,codigo_sucursal_id=1)

    def crearJefeTaller(usuario):
        JefeTaller.objects.create(username=usuario.username,password=usuario.password,is_superuser=usuario.is_superuser,first_name=usuario.first_name,last_name=usuario.last_name,email=usuario.email,is_staff=usuario.is_staff,is_active=usuario.is_active,cedula=usuario.cedula,direccion=usuario.direccion,fecha_de_nacimiento=usuario.fecha_de_nacimiento,telefono=usuario.telefono,codigo_sucursal_id=1)

    def crearGerente(usuario):
        NSucursal = Sucursal.objects.count() + 1
        Sucursal.objects.create(nombre='Sucursal '+str(NSucursal), direccion='Direccion '+str(NSucursal))
        Gerente.objects.create(username=usuario.username,password=usuario.password,is_superuser=usuario.is_superuser,first_name=usuario.first_name,last_name=usuario.last_name,email=usuario.email,is_staff=usuario.is_staff,is_active=usuario.is_active,cedula=usuario.cedula,direccion=usuario.direccion,fecha_de_nacimiento=usuario.fecha_de_nacimiento,telefono=usuario.telefono,codigo_sucursal_id=NSucursal)

class UserFormEliminate(forms.Form):
    usernameChoice = forms.ModelChoiceField(queryset=User.objects.all().filter(is_active=True).order_by('username'), to_field_name='username')

    def eliminate(usernameX):
        user = User.objects.get(username=usernameX)
        User.objects.filter(username=usernameX).update(is_active=False)

    def save(self):
        print("error")

class UserFormRecuperate(forms.Form):
    usernameChoice = forms.ModelChoiceField(queryset=User.objects.all().filter(is_active=False).order_by('username'), to_field_name='username')

    def recuperate(usernameX):
        user = User.objects.get(username=usernameX)
        User.objects.filter(username=usernameX).update(is_active=True)

    def save(self):
        print("error")

class UserFormModificate(forms.Form):

    usernameChoice = forms.ModelChoiceField(queryset=User.objects.all().filter(is_active=True).order_by('username'), to_field_name='username')

    def get(identificacion):
        usuario = User.objects.get(username=identificacion)
        return usuario

    def getID(identificacion):
        usuario = User.objects.get(id=identificacion)
        return usuario

    def actualizarAdministrador(usuario,identificacion):
        User.objects.filter(id=identificacion).update(first_name=usuario.first_name,last_name=usuario.last_name,email=usuario.email,cedula=usuario.cedula,direccion=usuario.direccion,fecha_de_nacimiento=usuario.fecha_de_nacimiento,telefono=usuario.telefono)

class UserFormAux(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'cedula',
            'direccion',
            'fecha_de_nacimiento',
            'telefono'
            )

class EmpleadoFormAux(forms.ModelForm):

    sucursalChoice = forms.ModelChoiceField(queryset=Sucursal.objects.all().order_by('nombre'))
    
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'email',
            'cedula',
            'direccion',
            'fecha_de_nacimiento',
            'telefono',
            'salario',
            )

    def actualizarVendedor(usuario, identificacion):
        Vendedor.objects.filter(id=identificacion).update(first_name=usuario.first_name,last_name=usuario.last_name,email=usuario.email,cedula=usuario.cedula,direccion=usuario.direccion,fecha_de_nacimiento=usuario.fecha_de_nacimiento,telefono=usuario.telefono,codigo_sucursal_id=usuario.sucursal,salario=usuario.salario)

    def actualizarGerente(usuario, identificacion):
        Gerente.objects.filter(id=identificacion).update(first_name=usuario.first_name,last_name=usuario.last_name,email=usuario.email,cedula=usuario.cedula,direccion=usuario.direccion,fecha_de_nacimiento=usuario.fecha_de_nacimiento,telefono=usuario.telefono,codigo_sucursal_id=usuario.sucursal,salario=usuario.salario)

    def actualizarJefeTaller(usuario, identificacion):
        JefeTaller.objects.filter(id=identificacion).update(first_name=usuario.first_name,last_name=usuario.last_name,email=usuario.email,cedula=usuario.cedula,direccion=usuario.direccion,fecha_de_nacimiento=usuario.fecha_de_nacimiento,telefono=usuario.telefono,codigo_sucursal_id=usuario.sucursal,salario=usuario.salario)