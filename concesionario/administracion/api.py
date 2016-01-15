from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from administracion.models import Empleado
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
        queryset = Empleado.objects.all()
        resource_name = 'empleado'
