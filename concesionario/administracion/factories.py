import factory
import factory.fuzzy
import datetime

from administracion import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

#Genera Superusuario
class SuperUserFactory(factory.Factory):

    class Meta:
        model = User

    username = 'admin'
    first_name = 'nombre'
    last_name = 'apellido'
    password = make_password(username)
    is_active = True
    is_staff = True
    is_superuser = True
    cedula = factory.fuzzy.FuzzyInteger(10000000, 999999999)
    direccion = factory.Faker('address')
    email = factory.Faker('email')
    fecha_de_nacimiento = factory.fuzzy.FuzzyDate(datetime.date(1950, 1, 1), datetime.date(2000, 12, 31))
    telefono = factory.fuzzy.FuzzyInteger(1000000, 9999999)

#===================================================
###Generadores de usuarios###
class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "Usuario%03d" % n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = make_password('Usuario')
    is_active = True
    cedula = factory.fuzzy.FuzzyInteger(10000000, 999999999)
    direccion = factory.Faker('address')
    email = factory.Faker('email')
    fecha_de_nacimiento = factory.fuzzy.FuzzyDate(datetime.date(1950, 1, 1), datetime.date(2000, 12, 31))
    telefono = factory.fuzzy.FuzzyInteger(1000000, 9999999)


#===================================================
#Generadores de Empleados
class EmpleadoFactory(UserFactory):

    class Meta:
        model = models.Empleado

    inicio_contrato = factory.fuzzy.FuzzyDate(datetime.date(2000, 1, 1))
    fin_contraro = factory.fuzzy.FuzzyDate(datetime.date(2016, 1, 1))
    salario = factory.fuzzy.FuzzyInteger(1000000, 9999999)


#===================================================
#Generador de Clientes
class ClienteFactory(UserFactory):
    class Meta:
        model = models.Cliente

    #id_usuario = factory.SubFactory(UserClienteFactory)
    username = factory.Sequence(lambda n: "Cliente%03d" % n)
    password = make_password('Cliente')
#===================================================

#===================================================
#Generador de Sucursales
class SucursalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Sucursal

    nombre = factory.Faker('company')
    direccion = factory.Faker('address')
#===================================================


#===================================================
#Genreador de Gerentes
class GerenteFactory(EmpleadoFactory):
    class Meta:
        model = models.Gerente
    username = factory.Sequence(lambda n: "Gerente%03d" % n)
    password = make_password('Gerente')
    codigo_sucursal = factory.SubFactory(SucursalFactory)
#===================================================


#===================================================
#Generador de Vendedores
class VendedorFactory(EmpleadoFactory):
    class Meta:
        model = models.Vendedor
    username = factory.Sequence(lambda n: "Vendedor%03d" % n)
    password = make_password('Vendedor')
    codigo_sucursal = factory.Iterator(models.Sucursal.objects.all())
    porcentaje_comision = factory.fuzzy.FuzzyInteger(1, 100)
#===================================================


#===================================================
#Generador de JefesTaller
class JefeTallerFactory(EmpleadoFactory):
    class Meta:
        model = models.JefeTaller
    username = factory.Sequence(lambda n: "JefeTaller%03d" % n)
    password = make_password('JefeTaller')
    codigo_sucursal = factory.Iterator(models.Sucursal.objects.all())
#===================================================



#===================================================
#Generador de Orden
class OrdenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Orden

    codigo_jefe_taller = factory.Iterator(models.JefeTaller.objects.all())
    diagnostico = factory.Faker('text', max_nb_chars=1200)
    estado = factory.fuzzy.FuzzyChoice(['C', 'T', 'E'])

#===================================================


#===================================================
#Generador de Repuesto
class RepuestoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Repuesto

    nombre = factory.Faker('word')
    descripcion = factory.Faker('text', max_nb_chars=300)
#===================================================


#===================================================
#Generador de RepuestosPorOrden
class RepuestosPorOrdenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.RepuestosPorOrden

    codigo_orden = factory.fuzzy.FuzzyChoice(models.Orden.objects.all())
    codigo_repuesto = factory.fuzzy.FuzzyChoice(models.Repuesto.objects.all())
    cantidad = factory.fuzzy.FuzzyInteger(1, 5)
#===================================================


#===================================================
#Generador de InventarioRepuestos
class InventarioRepuestoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.InventarioRepuesto

    codigo_repuesto = factory.Iterator(models.Repuesto.objects.all())
    cantidad = factory.fuzzy.FuzzyInteger(1, 50)
    precio_unidad = factory.fuzzy.FuzzyInteger(1000, 50000)
#===================================================



#===================================================
#Generador de Vehiculos
class VehiculoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Vehiculo

    marca = factory.fuzzy.FuzzyChoice(['Toyota', 'Chevrolet', 'Mazda', 'Hyundai', 'Ford', 'Nissan'])
    modelo = factory.fuzzy.FuzzyChoice(['X1', 'z350', 'F150', 'M91', 'ZX889', 'TX556'])
    descripcion = factory.Faker('text', max_nb_chars=200)
    imagen = factory.django.ImageField()

#===================================================


#===================================================
#Generador de RevisionVehiculo
class RevisionVehiculoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.RevisionVehiculo


    codigo_venta = factory.fuzzy.FuzzyChoice(models.Venta.objects.all())
    codigo_orden = factory.Iterator(models.Orden.objects.all())
    fecha_revision = factory.fuzzy.FuzzyDate(datetime.date(2015, 1, 1))
    kilometraje = factory.fuzzy.FuzzyInteger(1000, 999999)
    fecha_cambio_aceite = factory.fuzzy.FuzzyDate(datetime.date(2016, 1, 1))

#===================================================



#===================================================
#Generador de InventarioVehiculos
class InventarioVehiculoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.InventarioVehiculo

    codigo_vehiculo = factory.Iterator(models.Vehiculo.objects.all())
    color = factory.Faker('color_name')
    cantidad = factory.fuzzy.FuzzyInteger(1, 50)
    precio_unidad = factory.fuzzy.FuzzyInteger(30000000, 120000000)
#===================================================

#===================================================
#Generador de Ventas
class VentaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Venta

    codigo_vendedor = factory.fuzzy.FuzzyChoice(models.Vendedor.objects.all())
    codigo_cliente = factory.fuzzy.FuzzyChoice(models.Cliente.objects.all())
    codigo_vehiculo = factory.fuzzy.FuzzyChoice(models.Vehiculo.objects.all())
    porcentaje_descuento = factory.fuzzy.FuzzyInteger(1, 100)
    fecha_venta = factory.fuzzy.FuzzyDate(datetime.date(2016, 1, 1))
    placa = factory.Sequence(lambda n: "ABC%03d" % n)
#===================================================

#===================================================
#Generador de Cotizaciones
class CotizacionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Cotizacion

    codigo_vendedor = factory.fuzzy.FuzzyChoice(models.Vendedor.objects.all())
    codigo_vehiculo = factory.fuzzy.FuzzyChoice(models.Vehiculo.objects.all())
    fecha_cotizacion = factory.fuzzy.FuzzyDate(datetime.date(2016, 1, 1))
    porcentaje_descuento = factory.fuzzy.FuzzyInteger(1, 100)
#===================================================
