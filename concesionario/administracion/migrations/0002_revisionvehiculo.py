# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevisionVehiculo',
            fields=[
                ('codigo_revision', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=6)),
                ('fecha_revision', models.DateField()),
                ('kilometraje', models.PositiveIntegerField()),
                ('fecha_cambio_aceite', models.DateField()),
                ('codigo_cliente', models.ForeignKey(to='administracion.Cliente')),
                ('codigo_orden', models.OneToOneField(to='administracion.Orden')),
                ('codigo_vehiculo', models.ForeignKey(to='administracion.Vehiculo')),
            ],
        ),
    ]
