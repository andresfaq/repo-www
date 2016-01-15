# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_revisionvehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fin_contraro',
            field=models.DateField(max_length=8),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='inicio_contrato',
            field=models.DateField(max_length=8),
        ),
    ]
