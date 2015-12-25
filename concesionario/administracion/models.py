from django.db import models

from django.contrib.auth.models import User

# Con esto agregamos algunos campos al modelo User de django


User.add_to_class('cedula', models.PositiveIntegerField(null=True, blank=True))
User.add_to_class('direccion', models.CharField(max_length=100, null=True, blank=True))
User.add_to_class('fecha_de_nacimiento', models.DateTimeField(null=True, blank=True))
User.add_to_class('telefono', models.PositiveIntegerField(null=True, blank=True))


# Empleado hereda de usuario, por tanto hereda sus atributos
class empleado(User):

    id_empleado = models.AutoField(primary_key=True)
    # cedula = models.CharField(max_length=10, blank=True)
    # fecha_de_nacimiento = models.DateTimeField(max_length=8, blank=True)
    # direccion = models.CharField(max_length=100, blank=True)
    # telefono = models.PositiveIntegerField(null=True, blank=True)
    inicio_contrato = models.DateTimeField(max_length=8, blank=True)
    fin_contraro = models.DateTimeField(max_length=8, blank=True)
    salario = models.PositiveIntegerField(max_length=10, blank=True)