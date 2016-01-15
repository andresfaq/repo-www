from django.contrib import admin
from administracion import models
# Register your models here.

admin.site.register(models.Empleado)
admin.site.register(models.Vendedor)
admin.site.register(models.JefeTaller)
admin.site.register(models.Gerente)
admin.site.register(models.Cliente)
admin.site.register(models.Sucursal)