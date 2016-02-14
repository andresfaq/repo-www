from django import forms
from paginaweb.static import *
import datetime
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from administracion.models import Vehiculo, Cliente, Venta, Vendedor
import string
import random

class VehiculoFormAll(forms.Form):
    CHOICES1 = (('Hyundai','Hyundai'),( 'Chevrolet','Chevrolet'),('Mazda','Mazda'),('Toyota','Toyota'),('Nissan','Nissan'),('Ford','Ford'))
    marcaChoice = forms.ChoiceField(choices=CHOICES1)
    CHOICES2 = (('A','Ascendente'),('D','Descendente'))
    precioChoice = forms.ChoiceField(choices=CHOICES2)
    vehiculos = Vehiculo.objects.all()

    def vehiculosFiltro(marca, orden):
        if orden == 'A':
            vehiculos = Vehiculo.objects.all().filter(marca=marca).order_by('valor')
        else:
            vehiculos = Vehiculo.objects.all().filter(marca=marca).order_by('valor').reverse()
        return vehiculos

class VehiculoFormOne(forms.ModelForm):
    vehiculos = Vehiculo.objects.all()

    def get(codigo):
        vehiculo = Vehiculo.objects.get(codigo_vehiculo=codigo)
        return vehiculo

    def save(codigo_vehiculo,username,user,placa,descuento):
        cliente = Cliente.objects.get(username=username)
        vendido = True
        try:
            vendedor = Vendedor.objects.get(username=user.username)
        except:
            vendido = False
        else:
            Venta.objects.create(placa=placa,porcentaje_descuento=descuento,codigo_cliente_id=cliente.codigo_cliente,codigo_vehiculo_id=codigo_vehiculo,codigo_vendedor_id=vendedor.codigo_vendedor,sucursal_id=vendedor.codigo_sucursal_id,fecha_venta=datetime.datetime.now())
        return vendido

    def marcar(vehiculo):
        Vehiculo.objects.filter(codigo_vehiculo=vehiculo.codigo_vehiculo).update(cart=1)

    def cotizados():
        vehiculos = Vehiculo.objects.all().exclude(cart=0)
        return vehiculos

    def costoCotizados(cotizados):
        costo = 0
        for vehiculo in cotizados:
            costo = costo + vehiculo.valor
        return costo
    def borrarCotizados(cotizados):
        for cotizado in cotizados:
            Vehiculo.objects.filter(codigo_vehiculo=cotizado.codigo_vehiculo).update(cart=0)

class ClienteForm(forms.Form):
    clienteChoice = forms.ModelChoiceField(queryset=Cliente.objects.all().filter(is_active=True).order_by('username'), to_field_name='username')
    porcentaje_descuento = forms.IntegerField(max_value=100,min_value=0,widget=forms.NumberInput(attrs={'style': "width: 48px;"}))

    def generarPlaca():
        placa = ''.join(random.choice(string.ascii_uppercase) for _ in range(3)) + ''.join(random.choice(string.digits) for _ in range(3))
        return placa