from django.forms import widgets
from rest_framework import serializers
from administracion import models


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ('id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined' ,'cedula', 'direccion', 'fecha_de_nacimiento', 'telefono')

		def create(self, validated_data):
			return User.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.id = validated_data.get('id', instance.id)
			instance.password = validated_data.get('password', instance.password)
			instance.last_login = validated_data.get('last_login', instance.last_login)
			instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
			instance.username = validated_data.get('username', instance.username)
			instance.first_name = validated_data.get('first_name', instance.first_name)
			instance.last_name = validated_data.get('last_name', instance.last_name)
			instance.email = validated_data.get('email', instance.email)
			instance.is_staff = validated_data.get('is_staff', instance.is_staff)
			instance.is_active = validated_data.get('is_active', instance.is_active)
			instance.date_joined = validated_data.get('date_joined', instance.date_joined)
			instance.cedula = validated_data.get('cedula', instance.cedula)
			instance.direccion = validated_data.get('direccion', instance.direccion)
			instance.fecha_de_nacimiento = validated_data.get('fecha_de_nacimiento', instance.fecha_de_nacimiento)
			instance.telefono = validated_data.get('telefono', instance.telefono)
			instance.save()
			return instance

class EmpeadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Empleado
		fields = ('id_empleado', 'inicio_contrato', 'fin_contraro', 'salario')


		def create(self, validated_data):
			return Empleado.objects.create(**validated_data)

		def update(self, instance, validated_data):

			instance.id_empleado = validated_data.get('id_empleado', instance.id_empleado)
			instance.inicio_contrato = validated_data.get('inicio_contrato', instance.inicio_contrato)
			instance.fin_contraro = validated_data.get('fin_contraro', instance.fin_contraro)
			instance.salario = validated_data.get('salario', instance.salario)
			return instance

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Cliente
		fields = ('id_empleado')

		def create(self, validated_data):
			return Cliente.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_cliente = validated_data.get('codigo_cliente', instance.codigo_cliente)
			instance.save()
			return instance

class SucursalSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Sucursal
		fields = ('codigo_sucursal', 'nombre', 'direccion')

		def create(self, validated_data):
			return Sucursal.objects.create(**validated_data)

		def update(self, instance, validated_data):

			instance.codigo_sucursal = validated_data.get('codigo_sucursal', instance.codigo_sucursal)
			instance.nombre = validated_data.get('nombre', instance.nombre)
			instance.direccion = validated_data.get('direccion', instance.direccion)
			instance.save()
			return instance

class GerenteSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Gerente
		fields = ('codigo_gerente')

		def create(self, validated_data):
			return Gerente.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_gerente = validated_data.get('codigo_gerente', instance.codigo_gerente)
			instance.codigo_sucursal = validated_data.get('codigo_sucursal', instance.codigo_sucursal)
			instance.save()
			return instance

class VendedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Vendedor
		fields = ('codigo_vendedor', 'codigo_sucursal', 'porcentage_comision', 'salario')

		def create(self, validated_data):
			return Vendedor.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_vendedor = validated_data.get('codigo_vendedor', instance.codigo_vendedor)
			instance.codigo_sucursal = validated_data.get('codigo_sucursal', instance.codigo_sucursal)
			instance.porcentage_comision = validated_data.get('porcentage_comision', instance.porcentage_comision)
			instance.save()
			return instance

class JefeTallerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.JefeTaller
		fields = ('codigo_jefe_taller', 'codigo_sucursal', 'fin_contraro', 'salario')

		def create(self, validated_data):
			return JefeTaller.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_jefe_taller = validated_data.get('codigo_jefe_taller', instance.codigo_jefe_talller)
			instance.codigo_sucursal = validated_data.get('codigo_sucursal', instance.codigo_sucursal)
			instance.save()
			return instance

class OrdenSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Orden
		fields = ('codigo_orden', 'codigo_jefe_taller', 'diagnostico', 'estado')

		def create(self, validated_data):
			return Orden.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_orden = validated_data.get('codigo_orden', instance.codigo_orden)
			instance.codigo_jefe_taller = validated_data.get('codigo_jefe_taller', instance.codigo_jefe_taller)
			instance.diagnostico = validated_data.get('diagnostico', instance.diagnostico)
			instance.estado = validated_data.get('estado', instance.estado)
			instance.save()
			return instance

class RepuestoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Repuesto
		fields = ('codigo_repuesto', 'nombre', 'descripcion')

		def create(self, validated_data):
			return Repuesto.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_repuesto = validated_data.get('codigo_repuesto', instance.ccodigo_repuesto)
			instance.nombre = validated_data.get('nombre', instance.nombre)
			instance.descripcion = validated_data.get('descripcion', instance.descripcion)
			instance.save()
			return instance

class RepuestosPorOrdenSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RepuestosPorOrden
		fields = ('codigo_orden', 'codigo_repuesto', 'cantidad')

		def create(self, validated_data):
			return RepuestosPorOrden.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_orden = validated_data.get('codigo_orden', instance.codigo_orden)
			instance.codigo_repuesto = validated_data.get('codigo_repuesto', instance.codigo_repuesto)
			instance.cantidad = validated_data.get('cantidad', instance.cantidad)
			instance.save()
			return instance

class InventarioRepuestoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.InventarioRepuesto
		fields = ('codigo_inventario', 'codigo_repuesto', 'cantidad','precio_unidad')

		def create(self, validated_data):
			return InventarioRepuesto.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_inventario = validated_data.get('codigo_inventario', instance.codigo_inventario)
			instance.codigo_repuesto = validated_data.get('codigo_repuesto', instance.codigo_repuesto)
			instance.cantidad = validated_data.get('cantidad', instance.cantidad)
			instance.precio_unidad = validated_data.get('precio_unidad', instance.precio_unidad)
			instance.save()
			return instance

class VehiculoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Vehiculo
		fields = ('codigo_vehiculo', 'marca', 'modelo','descripcion','imagen')

		def create(self, validated_data):
			return VehiculoRepuesto.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_vehiculo = validated_data.get('codigo_vehiculo', instance.codigo_vehiculo)
			instance.marca = validated_data.get('marca', instance.marca)
			instance.modelo = validated_data.get('modelo', instance.modelo)
			instance.descripcion = validated_data.get('descripcion', instance.descripcion)
			instance.imagen = validated_data.get('imagen', instance.imagen)
			instance.save()
			return instance

class VentaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Cotizacion
		fields = ('codigo_venta', 'codigo_vendedor', 'codigo_cliente','codigo_vehiculo','placa','porcentage_descuento', 'fecha_venta')

		def create(self, validated_data):
			return Cotizacion.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_venta = validated_data.get('codigo_venta', instance.codigo_venta)
			instance.codigo_vendedor = validated_data.get('codigo_vendedor', instance.codigo_vendedor)
			instance.codigo_cliente = validated_data.get('codigo_cliente', instance.codigo_cliente)
			instance.codigo_vehiculo = validated_data.get('codigo_vehiculo', instance.codigo_vehiculo)
			instance.placa = validated_data.get('placa', instance.placa)
			instance.porcentage_descuento = validated_data.get('porcentage_descuento', instance.porcentage_descuento)
			instance.fecha_venta = validated_data.get('fecha_venta', instance.fecha_venta)
			instance.save()
			return instance

class CotizacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Cotizacion
		fields = ('codigo_cotizacion', 'codigo_vendedor', 'codigo_vehiculo','fecha_cotizacion','porcentage_descuento')

		def create(self, validated_data):
			return Cotizacion.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_cotizacion = validated_data.get('codigo_cotizacion', instance.codigo_cotizacion)
			instance.codigo_vendedor = validated_data.get('codigo_vendedor', instance.codigo_vendedor)
			instance.codigo_vehiculo = validated_data.get('codigo_vehiculo', instance.codigo_vehiculo)
			instance.fecha_cotizacion = validated_data.get('fecha_cotizacion', instance.fecha_cotizacion)
			instance.porcentage_descuento = validated_data.get('porcentage_descuento', instance.porcentage_descuento)
			instance.save()
			return instance

class InventarioVehiculoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.InventarioVehiculo
		fields = ('codigo_inventario', 'codigo_vehiculo','color','cantidad','precio_unidad')

		def create(self, validated_data):
			return InventarioVehiculo.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_inventario = validated_data.get('codigo_inventario', instance.codigo_inventario)
			instance.codigo_vehiculo = validated_data.get('codigo_vehiculo', instance.codigo_vehiculo)
			instance.color = validated_data.get('color', instance.color)
			instance.cantidad = validated_data.get('cantidad', instance.cantidad)
			instance.precio_unidad = validated_data.get('precio_unidad', instance.precio_unidad)
			instance.save()
			return instance

class RevisionVehiculoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RevisionVehiculo
		fields = ('codigo_revision', 'codigo_venta','codigo_orden','fecha_revision','kilometraje','fecha_cambio_aceite')

		def create(self, validated_data):
			return Revision.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.codigo_revision = validated_data.get('codigo_revision', instance.codigo_revision)
			instance.codigo_venta = validated_data.get('codigo_venta', instance.codigo_venta)
			instance.codigo_orden = validated_data.get('codigo_orden', instance.codigo_orden)
			instance.fecha_revision = validated_data.get('fecha_revision', instance.fecha_revision)
			instance.kilometraje = validated_data.get('kilometraje', instance.kilometraje)
			instance.fecha_cambio_aceite = validated_data.get('fecha_cambio_aceite', instance.fecha_cambio_aceite)
			instance.save()
			return instance