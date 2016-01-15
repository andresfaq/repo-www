# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_auto_20160115_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jefetaller',
            name='codigo_sucursal',
            field=models.ForeignKey(to='administracion.Sucursal'),
        ),
    ]
