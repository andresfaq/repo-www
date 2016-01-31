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
            'fecha_de_nacimiento',
            'telefono'
            )
    def identificacion():
        numID = User.objects.count()
        return numID

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

class UserFormModificateAux(forms.Form):

    usernameChoice = forms.ModelChoiceField(queryset=User.objects.all().filter(is_active=True).order_by('username'), to_field_name='username')

    def get(identificacion):
        usuario = User.objects.get(username=identificacion)
        return usuario