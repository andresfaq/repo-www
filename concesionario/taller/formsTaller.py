from django import forms
from paginaweb.static import *
import datetime
from functools import partial
from administracion.models import Orden,JefeTaller, Venta, RevisionVehiculo, Orden

class tallerForm(forms.Form):

    ESTADO_CHOICES=(('E','En espera'),( 'T','Terminada'),('C','Cancelada'),)
    diagnostico=forms.CharField(widget=forms.Textarea(attrs={'class' : ''}),label="Diagnostico")
    estado=forms.ChoiceField(choices=ESTADO_CHOICES,label="Estado Orden")
    jefeTaller = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}),label="Jefe Taller Encargado ")
    sucursal = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}),label="Sucursal ")
    fechaRevision =forms.DateField(initial=datetime.date.today)
    codigoVenta = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}),label="Codigo de Venta ")
    kmVehiculo = forms.CharField(widget=forms.TextInput(),label="Kilometraje del vehiculo ")
    fechaCAceite = forms.DateField(initial=datetime.date.today)
    buscarVenta = forms.CharField(label="Cliente ",required = False)



    def clean_diagnostico(self):
        mensaje = self.cleaned_data['diagnostico']
        num_palabras = len(mensaje.split())
        if num_palabras < 4:
            raise forms.ValidationError("Se requieren minimo 4 palabras!")
        return mensaje

    def clean_codigoVenta(self):
        dato = int(self.cleaned_data['codigoVenta'])
        return dato

    def getEstado(idX):
            #placa(Venta) -> codigo_venta(Venta)-> codigo_venta_id(RevisionVehiculo) -> codigo_orden_id(RevisionVehiculo) -> codigo_orden(Orden) -> estado(Orden)
        carros=RevisionVehiculo.objects.select_related('codigo_orden','codigo_venta')
        estado = "None"

        for carro in carros:
            if carro.codigo_venta.placa == idX:
                estado = carro.codigo_orden.estado

        if estado == 'T':
            estado = 'Terminado'
        elif estado == 'C':
            estado = 'Cancelado'
        elif estado == 'E':
            estado = 'En espera'
        else:
            estado = 'ERROR'
        return estado


'''
class tallerRepuesto(forms.Form):
    inpNombre= forms.CharField(widget=forms.TextInput())
    inpDescripcion= forms.CharField(widget=forms.TextInput())
    inpDescripcion= forms.CharField(widget=forms.TextInput())
'''
