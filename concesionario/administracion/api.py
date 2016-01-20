from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields, utils
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
        excludes = ['password', 'is_active', 'is_staff', 'is_superuser']

class VendedorResource(ModelResource):
    class Meta:
        queryset = models.Vendedor.objects.all()
        resource_name = 'vendedor'
        excludes = ['password', 'is_active', 'is_staff', 'is_superuser']

class JefeTallerResource(ModelResource):
    class Meta:
        queryset = models.JefeTaller.objects.all()
        resource_name = 'jefetaller'
        excludes = ['password', 'is_active', 'is_staff', 'is_superuser']

class ClienteResource(ModelResource):
    class Meta:
        queryset = models.Cliente.objects.all()
        resource_name = 'cliente'



class OrdenResource(ModelResource):
    class Meta:
        queryset = models.Orden.objects.all()
        resource_name = 'orden'
        filtering = {
            'estado': ALL_WITH_RELATIONS,
        }





#===== API Modulo Clientes =====#

class DatosVehiculoResource(ModelResource):
    codigo_orden = fields.OneToOneField(OrdenResource, 'codigo_orden')

    class Meta:
        queryset = models.RevisionVehiculo.objects.all()
        resource_name = 'datosvehiculo'
        excludes = ['codigo_revision', 'codigo_venta', 'codigo_orden', ]
        filtering = {
            'codigo_orden': ALL,
            #'user': ALL_WITH_RELATIONS,
            #'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }

