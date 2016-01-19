# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuestospororden',
            name='cantidad',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
    ]
