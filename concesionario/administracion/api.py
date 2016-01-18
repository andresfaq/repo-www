from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from administracion import models
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'usuario'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }

class EmpleadoResource(ModelResource):
    class Meta:
        queryset = models.Empleado.objects.all()
        resource_name = 'empleado'

class GerenteResource(ModelResource):
    class Meta:
        queryset = models.Gerente.objects.all()
        resource_name = 'gerente'

class VendedorResource(ModelResource):
    class Meta:
        queryset = models.Vendedor.objects.all()
        resource_name = 'vendedor'

class JefeTallerResource(ModelResource):
    class Meta:
        queryset = models.JefeTaller.objects.all()
        resource_name = 'jefetaller'

class ClienteResource(ModelResource):
    class Meta:
        queryset = models.Cliente.objects.all()
        resource_name = 'cliente'
