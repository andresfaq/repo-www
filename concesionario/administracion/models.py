from django.db import models

from django.contrib.auth.models import User



class empleado(models.Model):

    user = models.ForeignKey(User, unique=True)
    id_empleado = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, blank=True)
    fecha_de_nacimiento = models.DateTimeField(max_lengt=8, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
    inicio_contrato = models.DateTimeField(max_length=8, blank=True)
    fin_contraro = models.DateTimeField(max_length=8, blank=True)
    salario = models.PositiveIntegerField(max_length=10, blank=True)