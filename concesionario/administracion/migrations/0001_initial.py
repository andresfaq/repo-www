# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_auto_20160102_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, parent_link=True, auto_created=True)),
                ('codigo_cliente', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
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
                ('porcentaje_descuento', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, parent_link=True, auto_created=True)),
                ('id_empleado', models.AutoField(serialize=False, primary_key=True)),
                ('inicio_contrato', models.DateTimeField(max_length=8)),
                ('fin_contraro', models.DateTimeField(max_length=8)),
                ('salario', models.PositiveIntegerField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
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
                ('diagnostico', models.CharField(null=True, max_length=2000, blank=True)),
                ('estado', models.CharField(max_length=1, choices=[('C', 'Cancelada'), ('T', 'Terminada'), ('E', 'En Espera')])),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('codigo_repuesto', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(null=True, max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RepuestosPorOrden',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('codigo_orden', models.ForeignKey(to='administracion.Orden')),
                ('codigo_repuesto', models.ForeignKey(to='administracion.Repuesto')),
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
                ('descripcion', models.CharField(null=True, max_length=200, blank=True)),
                ('imagen', models.ImageField(upload_to='vehiculos/')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('codigo_venta', models.AutoField(serialize=False, primary_key=True)),
                ('porcentaje_descuento', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=0)),
                ('codigo_cliente', models.ForeignKey(to='administracion.Cliente')),
                ('codigo_vehiculo', models.ForeignKey(to='administracion.Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('empleado_ptr', models.OneToOneField(to='administracion.Empleado', parent_link=True, auto_created=True)),
                ('codigo_gerente', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('administracion.empleado',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='JefeTaller',
            fields=[
                ('empleado_ptr', models.OneToOneField(to='administracion.Empleado', parent_link=True, auto_created=True)),
                ('codigo_jefe_taller', models.AutoField(serialize=False, primary_key=True)),
                ('codigo_sucursal', models.OneToOneField(to='administracion.Sucursal')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('administracion.empleado',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('empleado_ptr', models.OneToOneField(to='administracion.Empleado', parent_link=True, auto_created=True)),
                ('codigo_vendedor', models.AutoField(serialize=False, primary_key=True)),
                ('codigo_sucursal', models.ForeignKey(to='administracion.Sucursal')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('administracion.empleado',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
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
