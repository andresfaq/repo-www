from django import forms
from paginaweb.static import *
import datetime
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
#from administracion.models import Orden,JefeTaller

class crearUsuarioForm(forms.Form):
    
    usuario = forms.CharField(max_length=30, required=True)
    contrasenaUsuario = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'type': 'password'}), required=True)
    TIPO_CHOICES=(('A','Aministrador'),( 'G','Gerente'),('J','Jefe de taller'),( 'V','Vendedor'))
    tipoUsuario=forms.ChoiceField(choices=TIPO_CHOICES,label="Tipo de usuario")

    nombres = forms.CharField(max_length=30, required=True)
    apellidos = forms.CharField(max_length=30, required=True)
    cedula = forms.IntegerField(widget=forms.TextInput(attrs={'maxlength': '15' , 'data-mask' : '999999999999999'}), required=True)
    email = forms.EmailField(max_length=254, required=True)
    fecha = forms.DateField(required=True)
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={'maxlength': '15', 'data-mask' : '999999999999999'}), required=True)