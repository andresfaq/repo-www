# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_auto_20151229_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gerente',
            name='empleado_ptr',
            field=models.OneToOneField(to='administracion.Empleado', parent_link=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='inventariorepuesto',
            name='codigo_repuesto',
            field=models.OneToOneField(to='administracion.Repuesto'),
        ),
        migrations.AlterField(
            model_name='jefetaller',
            name='codigo_sucursal',
            field=models.OneToOneField(to='administracion.Sucursal'),
        ),
        migrations.AlterField(
            model_name='jefetaller',
            name='empleado_ptr',
            field=models.OneToOneField(to='administracion.Empleado', parent_link=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='empleado_ptr',
            field=models.OneToOneField(to='administracion.Empleado', parent_link=True, auto_created=True),
        ),
    ]
