from django import forms
from paginaweb.static import *
import datetime
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from administracion.models import Orden,JefeTaller

class tallerForm(forms.Form):

    ESTADO_CHOICES=(('E','En espera'),( 'T','Terminada'),('C','Cancelada'),)
    diagnostico=forms.CharField(widget=forms.Textarea(attrs={'class' : ''}),label="Diagnostico")
    estado=forms.ChoiceField(choices=ESTADO_CHOICES,label="Estado Orden")
    jefeTaller= forms.ModelChoiceField(queryset=JefeTaller.objects.all().order_by('first_name'),
                                       to_field_name='codigo_jefe_taller')
    '''jefeTaller= forms.ModelChoiceField(queryset=JefeTaller.objects.all().order_by('first_name').values_list('first_name',flat=True),
                                       to_field_name="codigo_jefe_taller",
                                       empty_label="Seleccione Jefe encargado",
                                       widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))
    '''
    fechaRevision =forms.DateField(initial=datetime.date.today)
    codigoVenta=forms.CharField(widget=forms.TextInput(attrs={'readonly': True}),label="Codigo de Venta ")

    buscarVenta = forms.CharField(label="Cliente ")



    def clean_diagnostico(self):
        mensaje = self.cleaned_data['diagnostico']
        num_palabras = len(mensaje.split())
        if num_palabras < 4:
            raise forms.ValidationError("Se requieren minimo 4 palabras!")
        return mensaje



'''
    class Meta:
        model = Vehiculo
        fields = '__all__'
'''

