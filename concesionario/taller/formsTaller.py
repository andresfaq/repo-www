from django import forms
from paginaweb.static import *
import datetime
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class tallerForm(forms.Form):

    ESTADO_CHOICES=(('En Espera','En espera'),( 'Terminada','Terminada'),('Cancelada','Cancelada'),)
    diagnostico=forms.CharField(widget=forms.Textarea(attrs={'class' : ''}),label="Diagnostico")
    estado=forms.ChoiceField(choices=ESTADO_CHOICES,label="Estado Orden")
    jefeTaller= forms.Select()
    fechaRevision =forms.DateField(initial=datetime.date.today)


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

