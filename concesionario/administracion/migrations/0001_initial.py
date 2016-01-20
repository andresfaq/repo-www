# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_auto_20160115_0419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('codigo_cotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_cotizacion', models.DateField()),
                ('porcentaje_descuento', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('inicio_contrato', models.DateField(null=True, max_length=8)),
                ('fin_contraro', models.DateField(null=True, max_length=8)),
                ('salario', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='InventarioRepuesto',
            fields=[
                ('codigo_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InventarioVehiculo',
            fields=[
                ('codigo_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=50)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('codigo_orden', models.AutoField(primary_key=True, serialize=False)),
                ('diagnostico', models.CharField(blank=True, null=True, max_length=2000)),
                ('estado', models.CharField(choices=[('C', 'Cancelada'), ('T', 'Terminada'), ('E', 'En Espera')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('codigo_repuesto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, null=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='RepuestosPorOrden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField()),
                ('codigo_orden', models.ForeignKey(to='administracion.Orden')),
                ('codigo_repuesto', models.ForeignKey(to='administracion.Repuesto')),
            ],
        ),
        migrations.CreateModel(
            name='RevisionVehiculo',
            fields=[
                ('codigo_revision', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_revision', models.DateField()),
                ('kilometraje', models.PositiveIntegerField()),
                ('fecha_cambio_aceite', models.DateField()),
                ('codigo_orden', models.OneToOneField(to='administracion.Orden')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('codigo_sucursal', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('codigo_vehiculo', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, null=True, max_length=200)),
                ('imagen', models.ImageField(upload_to='vehiculos/')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('codigo_venta', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=6)),
                ('porcentaje_descuento', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=0)),
                ('fecha_venta', models.DateField()),
                ('codigo_vehiculo', models.ForeignKey(to='administracion.Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='administracion.Empleado')),
                ('codigo_cliente', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('administracion.empleado',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='administracion.Empleado')),
                ('codigo_gerente', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_sucursal', models.OneToOneField(to='administracion.Sucursal')),
            ],
            options={
                'verbose_name': 'Gerente',
                'verbose_name_plural': 'Gerentes',
            },
            bases=('administracion.empleado',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='JefeTaller',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='administracion.Empleado')),
                ('codigo_jefe_taller', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_sucursal', models.ForeignKey(to='administracion.Sucursal')),
            ],
            options={
                'verbose_name': 'Jefe Taller',
                'verbose_name_plural': 'Jefes Taller',
            },
            bases=('administracion.empleado',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='administracion.Empleado')),
                ('codigo_vendedor', models.AutoField(primary_key=True, serialize=False)),
                ('porcentaje_comision', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=0)),
                ('codigo_sucursal', models.ForeignKey(to='administracion.Sucursal')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
            },
            bases=('administracion.empleado',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='revisionvehiculo',
            name='codigo_venta',
            field=models.ForeignKey(to='administracion.Venta'),
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
            model_name='cotizacion',
            name='codigo_vehiculo',
            field=models.ForeignKey(to='administracion.Vehiculo'),
        ),
        migrations.AddField(
            model_name='venta',
            name='codigo_cliente',
            field=models.ForeignKey(to='administracion.Cliente'),
        ),
        migrations.AddField(
            model_name='venta',
            name='codigo_vendedor',
            field=models.ForeignKey(to='administracion.Vendedor'),
        ),
        migrations.AddField(
            model_name='orden',
            name='codigo_jefe_taller',
            field=models.ForeignKey(to='administracion.JefeTaller'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='codigo_vendedor',
            field=models.ForeignKey(to='administracion.Vendedor'),
        ),
    ]
