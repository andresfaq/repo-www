# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo_cliente', models.AutoField(serialize=False, primary_key=True)),
                ('id_usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('codigo_cotizacion', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_cotizacion', models.DateField()),
                ('porcentaje_descuento', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(serialize=False, primary_key=True)),
                ('inicio_contrato', models.DateField(max_length=8)),
                ('fin_contraro', models.DateField(max_length=8)),
                ('salario', models.PositiveIntegerField()),
                ('id_usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('codigo_gerente', models.AutoField(serialize=False, primary_key=True)),
                ('codigo_empleado', models.OneToOneField(to='administracion.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='InventarioRepuesto',
            fields=[
                ('codigo_inventario', models.AutoField(serialize=False, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InventarioVehiculo',
            fields=[
                ('codigo_inventario', models.AutoField(serialize=False, primary_key=True)),
                ('color', models.CharField(max_length=50)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JefeTaller',
            fields=[
                ('codigo_jefe_taller', models.AutoField(serialize=False, primary_key=True)),
                ('codigo_empleado', models.OneToOneField(to='administracion.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('codigo_orden', models.AutoField(serialize=False, primary_key=True)),
                ('diagnostico', models.CharField(blank=True, max_length=2000, null=True)),
                ('estado', models.CharField(choices=[('C', 'Cancelada'), ('T', 'Terminada'), ('E', 'En Espera')], max_length=1)),
                ('codigo_jefe_taller', models.ForeignKey(to='administracion.JefeTaller')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('codigo_repuesto', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RepuestosPorOrden',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('codigo_orden', models.ForeignKey(to='administracion.Orden')),
                ('codigo_repuesto', models.ForeignKey(to='administracion.Repuesto')),
            ],
        ),
        migrations.CreateModel(
            name='RevisionVehiculo',
            fields=[
                ('codigo_revision', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_revision', models.DateField()),
                ('kilometraje', models.PositiveIntegerField()),
                ('fecha_cambio_aceite', models.DateField()),
                ('codigo_orden', models.OneToOneField(to='administracion.Orden')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('codigo_sucursal', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('codigo_vehiculo', models.AutoField(serialize=False, primary_key=True)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('imagen', models.ImageField(upload_to='vehiculos/')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('codigo_vendedor', models.AutoField(serialize=False, primary_key=True)),
                ('codigo_empleado', models.OneToOneField(to='administracion.Empleado')),
                ('codigo_sucursal', models.ForeignKey(to='administracion.Sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('codigo_venta', models.AutoField(serialize=False, primary_key=True)),
                ('placa', models.CharField(max_length=6)),
                ('porcentaje_descuento', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('fecha_venta', models.DateField()),
                ('codigo_cliente', models.ForeignKey(to='administracion.Cliente')),
                ('codigo_vehiculo', models.ForeignKey(to='administracion.Vehiculo')),
                ('codigo_vendedor', models.ForeignKey(to='administracion.Vendedor')),
            ],
        ),
        migrations.AddField(
            model_name='revisionvehiculo',
            name='codigo_venta',
            field=models.ForeignKey(to='administracion.Venta'),
        ),
        migrations.AddField(
            model_name='jefetaller',
            name='codigo_sucursal',
            field=models.ForeignKey(to='administracion.Sucursal'),
        ),
        migrations.AddField(
            model_name='inventariovehiculo',
            name='codigo_vehiculo',
            field=models.ForeignKey(to='administracion.Vehiculo'),
        ),
        migrations.AddField(
            model_name='inventariorepuesto',
            name='codigo_repuesto',
            field=models.OneToOneField(to='administracion.Repuesto'),
        ),
        migrations.AddField(
            model_name='gerente',
            name='codigo_sucursal',
            field=models.OneToOneField(to='administracion.Sucursal'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='codigo_vehiculo',
            field=models.ForeignKey(to='administracion.Vehiculo'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='codigo_vendedor',
            field=models.ForeignKey(to='administracion.Vendedor'),
        ),
    ]
