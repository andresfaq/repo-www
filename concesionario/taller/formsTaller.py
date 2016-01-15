from django import forms
from administracion.models import  Vehiculo

class tallerForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = '__all__'


