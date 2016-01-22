# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_auto_20160122_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('codigo_cliente', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
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
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('id_empleado', models.AutoField(serialize=False, primary_key=True)),
                ('inicio_contrato', models.DateField(null=True, max_length=8)),
                ('fin_contraro', models.DateField(null=True, max_length=8)),
                ('salario', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
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
            name='Orden',
            fields=[
                ('codigo_orden', models.AutoField(serialize=False, primary_key=True)),
                ('diagnostico', models.CharField(blank=True, max_length=2000, null=True)),
                ('estado', models.CharField(max_length=1, choices=[('C', 'Cancelada'), ('T', 'Terminada'), ('E', 'En Espera')])),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cantidad', models.PositiveIntegerField()),
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
            options={
                'verbose_name_plural': 'Sucursales',
                'verbose_name': 'Sucursal',
            },
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
            name='Venta',
            fields=[
                ('codigo_venta', models.AutoField(serialize=False, primary_key=True)),
                ('placa', models.CharField(max_length=6)),
                ('porcentaje_descuento', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('fecha_venta', models.DateField()),
                ('codigo_cliente', models.ForeignKey(to='administracion.Cliente')),
                ('codigo_vehiculo', models.ForeignKey(to='administracion.Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='administracion.Empleado')),
                ('codigo_gerente', models.AutoField(serialize=False, primary_key=True)),
                ('codigo_sucursal', models.OneToOneField(to='administracion.Sucursal')),
            ],
            options={
                'verbose_name_plural': 'Gerentes',
                'verbose_name': 'Gerente',
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
                ('codigo_jefe_taller', models.AutoField(serialize=False, primary_key=True)),
                ('codigo_sucursal', models.ForeignKey(to='administracion.Sucursal')),
            ],
            options={
                'verbose_name_plural': 'Jefes Taller',
                'verbose_name': 'Jefe Taller',
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
                ('codigo_vendedor', models.AutoField(serialize=False, primary_key=True)),
                ('porcentaje_comision', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('codigo_sucursal', models.ForeignKey(to='administracion.Sucursal')),
            ],
            options={
                'verbose_name_plural': 'Vendedores',
                'verbose_name': 'Vendedor',
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
