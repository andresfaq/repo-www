from django import forms
from administracion.models import  Vehiculo

class tallerForm(forms.Form):

    codigoOrden=forms.CharField(max_length=35,label="Codigo Orden")
    diagnostico=forms.CharField(widget=forms.Textarea,label="Diagnostico")
    estado=forms.CharField(max_length=1,label="Mensaje")
    jefeTaller=forms.Select()


    def clean_diagnostico(self):
        mensaje = self.cleaned_data['mensaje']
        num_palabras = len(mensaje.split())
        if num_palabras < 4:
            raise forms.ValidationError("Se requieren minimo 4 palabras!")
        return mensaje


'''
    class Meta:
        model = Vehiculo
        fields = '__all__'
'''

