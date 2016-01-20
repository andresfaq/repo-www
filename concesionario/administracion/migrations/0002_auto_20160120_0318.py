# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fin_contraro',
            field=models.DateField(null=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='inicio_contrato',
            field=models.DateField(null=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='salario',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
