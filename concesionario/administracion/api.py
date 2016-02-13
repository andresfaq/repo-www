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
        excludes = ['password', 'is_active', 'is_staff', 'is_superuser']



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




#===== API Modulo Clientes =====#

# http://localhost:8000/administracion/api/v1/ordenmovil/?format=json&cedula__exact=298547509

class DatosOrdenMovilResource(ModelResource):
    #codigo_orden = fields.OneToOneField(OrdenResource, 'codigo_orden')

    class Meta:
        #Hay cliente = models.Cliente.objects.get(codigo_cliente=503).venta_set.all()
        var = models.Cliente.objects.all()
        queryset = var
        resource_name = 'ordenmovil'
        #excludes = ['codigo_revision', 'codigo_venta', 'codigo_orden', ]
        filtering = {
            'cedula': ALL
            #'codigo_orden': ALL,
            #'user': ALL_WITH_RELATIONS,
            #'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }



#Se va a usar para sacar la lista con las placas de los vehiculos de un cliente
#http://localhost:8000/administracion/api/v1/datosventas/?format=json&usuario=Cliente001
class DatosVentasClienteResource(ModelResource):

    class Meta:
        ventas = models.Venta.objects.all()
        queryset = ventas
        resource_name = 'datosventas'

    def obj_get_list(self, bundle, **kwargs):
        cliente = bundle.request.GET['usuario']
        ventas = models.Cliente.objects.get(username=cliente).venta_set.all()
        return ventas




#Se va a usar para obtener las revisiones de un vehiculo en particular
#http://localhost:8000/administracion/api/v1/datosrevision/?format=json&cod_ven=58
class DatosRevisionesVehiculoResource(ModelResource):

    class Meta:
        ventas = models.RevisionVehiculo.objects.all()
        queryset = ventas
        resource_name = 'datosrevision'

    def obj_get_list(self, bundle, **kwargs):
        param = bundle.request.GET['cod_ven']
        ventas = models.RevisionVehiculo.objects.filter(codigo_venta=param)
        return ventas