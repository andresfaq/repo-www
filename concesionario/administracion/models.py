from django.db import models
from django.contrib.auth.models import User

# Validadores -> Solo funcionan con los ModelForm de django
from django.core.validators import MinValueValidator, MaxValueValidator

# Para gestionar la eliminacion de imagenes cuando se elimina un vehiculo en la BD
from django.db.models.signals import post_delete
from django.dispatch import receiver



# Con esto agregamos algunos campos al modelo User de django
User.add_to_class('cedula', models.PositiveIntegerField(null=True))
User.add_to_class('direccion', models.CharField(max_length=100, null=True))
User.add_to_class('fecha_de_nacimiento', models.DateTimeField(null=True))
User.add_to_class('telefono', models.PositiveIntegerField(null=True))


# Empleado hereda de usuario, por tanto hereda sus atributos
class Empleado(User):

    id_empleado = models.AutoField(primary_key=True)
    inicio_contrato = models.DateTimeField(max_length=8)
    fin_contraro = models.DateTimeField(max_length=8)
    salario = models.PositiveIntegerField(max_length=10)

class Cliente(User):
    codigo_cliente = models.AutoField(primary_key=True)


class Gerente(Empleado):
    codigo_gerente = models.AutoField(primary_key=True)


class Sucursal(models.Model):
    codigo_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length=150, null=False)


class Vendedor(Empleado):
    codigo_vendedor = models.AutoField(primary_key=True)
    codigo_sucursal = models.ForeignKey(Sucursal)

class JefeTaller(Empleado):
    codigo_jefe_taller = models.AutoField(primary_key=True)
    codigo_sucursal = models.OneToOneField(Sucursal)


class Orden(models.Model):
    ESTADOS = (
        ('C', 'Cancelada'),
        ('T', 'Terminada'),
        ('E', 'En Espera'),
    )

    codigo_orden = models.AutoField(primary_key=True)
    codigo_jefe_taller = models.ForeignKey(JefeTaller)
    diagnostico = models.CharField(max_length=2000, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADOS)


class Repuesto(models.Model):
    codigo_repuesto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300, null=True, blank=True)


class RepuestosPorOrden(models.Model):
    codigo_orden = models.ForeignKey(Orden)
    codigo_repuesto = models.ForeignKey(Repuesto)





class InventarioRepuesto(models.Model):
    codigo_inventario = models.AutoField(primary_key=True)
    codigo_repuesto = models.OneToOneField(Repuesto)
    cantidad = models.PositiveIntegerField()
    precio_unidad = models.PositiveIntegerField()



class Vehiculo(models.Model):
    codigo_vehiculo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, null=False)
    modelo = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to='vehiculos/') # Ver settings.py MEDIA_ROOT para ver el directorio donde se guardan las imagenes


class Venta(models.Model):
    codigo_venta = models.AutoField(primary_key=True)
    codigo_vendedor = models.ForeignKey(Vendedor)
    codigo_cliente = models.ForeignKey(Cliente)
    codigo_vehiculo = models.ForeignKey(Vehiculo)
    porcentaje_descuento = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])


class Cotizacion(models.Model):
    codigo_cotizacion = models.AutoField(primary_key=True)
    codigo_vendedor = models.ForeignKey(Vendedor)
    codigo_vehiculo = models.ForeignKey(Vehiculo)
    fecha_cotizacion = models.DateField()
    porcentaje_descuento = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])



class InventarioVehiculo(models.Model):
    codigo_inventario = models.AutoField(primary_key=True)
    codigo_vehiculo = models.ForeignKey(Vehiculo)
    color = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    precio_unidad = models.PositiveIntegerField()


class RevisionVehiculo():
    codigo_revision = models.AutoField(primary_key=True)
    codigo_cliente = models.ForeignKey(Cliente)
    codigo_vehiculo = models.ForeignKey(Vehiculo)
    codigo_orden = models.OneToOneField(Orden)
    placa = models.CharField(max_length=6)
    fecha_revision = models.DateField()
    kilometraje = models.PositiveIntegerField()
    fecha_cambio_aceite = models.DateField()

#Borra las imagenes de los registros de vehiculos que se eliminan
@receiver(post_delete, sender=Vehiculo)
def img_vehiculo_delete(sender, instance, **kwargs):
    instance.photo.delete(False)