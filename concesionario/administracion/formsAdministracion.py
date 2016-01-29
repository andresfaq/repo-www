from django import forms
from paginaweb.static import *
import datetime
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from administracion.models import User

class UserForm(forms.ModelForm):
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
            #'fecha_de_nacimiento',
            'telefono'
            )