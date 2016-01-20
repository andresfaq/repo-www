# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_auto_20160120_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='inicio_contrato',
            field=models.DateField(null=True, max_length=8),
        ),
    ]
