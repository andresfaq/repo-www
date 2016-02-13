from django import forms
from paginaweb.static import *
import datetime
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from administracion.models import Vehiculo, Cliente, Venta, Vendedor

class VehiculoFormAll(forms.Form):
    vehiculos = Vehiculo.objects.all()

class VehiculoFormOne(forms.Form):
    vehiculos = Vehiculo.objects.all()

    def get(codigo):
        vehiculo = Vehiculo.objects.get(codigo_vehiculo=codigo)
        return vehiculo

    def save(codigo_vehiculo,username,user):
        cliente = Cliente.objects.get(username=username)
        vendedor = Vendedor.objects.get(username=user.username)
        Venta.objects.create(codigo_cliente_id=cliente.codigo_cliente,codigo_vehiculo_id=codigo_vehiculo,codigo_vendedor_id=vendedor.codigo_vendedor,sucursal_id=vendedor.codigo_sucursal_id,fecha_venta=datetime.datetime.now())

class ClienteForm(forms.Form):
    clienteChoice = forms.ModelChoiceField(queryset=Cliente.objects.all().filter(is_active=True).order_by('username'), to_field_name='username')