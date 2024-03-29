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
User.add_to_class('fecha_de_nacimiento', models.DateField(null=True))
User.add_to_class('telefono', models.PositiveIntegerField(null=True))


# Empleado hereda de usuario, por tanto hereda sus atributos
class Empleado(User):
    #id_usuario = models.OneToOneField(User)
    id_empleado = models.AutoField(primary_key=True)
    inicio_contrato = models.DateField(max_length=8, null=True)
    fin_contraro = models.DateField(max_length=8, null=True)
    salario = models.PositiveIntegerField(null=True)

#    def __str__(self):
#        return str(self.id_usuario)

class Cliente(User):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    #id_usuario = models.OneToOneField(User)
    codigo_cliente = models.AutoField(primary_key=True)

#    def __str__(self):
#        return str(self.codigo_cliente)


class Sucursal(models.Model):
    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'

    codigo_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False,unique=True)
    direccion = models.CharField(max_length=150, null=False)

    def __str__(self):
        return str(self.nombre)

    def getCodigoS(self):
        return self.codigo_sucursal

class Gerente(Empleado):
    class Meta:
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'

    #codigo_empleado = models.OneToOneField(Empleado)
    codigo_gerente = models.AutoField(primary_key=True)
    codigo_sucursal = models.OneToOneField(Sucursal)


#    def __str__(self):
#        return str(self.codigo_empleado)

class Vendedor(Empleado):
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    #codigo_empleado = models.OneToOneField(Empleado)
    codigo_vendedor = models.AutoField(primary_key=True)
    codigo_sucursal = models.ForeignKey(Sucursal)
    porcentaje_comision = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])

#    def __str__(self):
#        return str(self.codigo_empleado)

class JefeTaller(Empleado):
    class Meta:
        verbose_name = 'Jefe Taller'
        verbose_name_plural = 'Jefes Taller'

    #codigo_empleado = models.OneToOneField(Empleado)
    codigo_jefe_taller = models.AutoField(primary_key=True)
    codigo_sucursal = models.ForeignKey(Sucursal)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


#    def __str__(self):
#        return str(self.codigo_empleado)


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
    sucursal = models.ForeignKey(Sucursal)
    #codigo_cliente = models.ForeignKey(Cliente)


class Repuesto(models.Model):
    codigo_repuesto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300, null=True, blank=True)


class RepuestosPorOrden(models.Model):
    codigo_orden = models.ForeignKey(Orden)
    codigo_repuesto = models.ForeignKey(Repuesto)
    cantidad = models.PositiveIntegerField()



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
    #imagen = models.ImageField(upload_to='vehiculos/') # Ver settings_old.py MEDIA_ROOT para ver el directorio donde se guardan las imagenes
    cart = models.IntegerField(null=False, default=0)

    def __str__(self):
        return str(self.modelo + " - " + self.marca)


class Venta(models.Model):
    codigo_venta = models.AutoField(primary_key=True)
    codigo_vendedor = models.ForeignKey(Vendedor)
    codigo_cliente = models.ForeignKey(Cliente)
    codigo_vehiculo = models.ForeignKey(Vehiculo)
    placa = models.CharField(max_length=6)
    porcentaje_descuento = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    fecha_venta = models.DateField()
    sucursal = models.ForeignKey(Sucursal)


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


class RevisionVehiculo(models.Model):
    codigo_revision = models.AutoField(primary_key=True)
    codigo_venta = models.ForeignKey(Venta)
    codigo_orden = models.OneToOneField(Orden)
    fecha_revision = models.DateField()
    kilometraje = models.PositiveIntegerField()
    fecha_cambio_aceite = models.DateField()

#Borra las imagenes de los registros de vehiculos que se eliminan
#@receiver(post_delete, sender=Vehiculo)
#def img_vehiculo_delete(sender, instance, **kwargs):
    #instance.photo.delete(False)
    #instance.photo.delete(True)



