# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_auto_20151225_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, parent_link=True, auto_created=True)),
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('inicio_contrato', models.DateTimeField(blank=True, max_length=8)),
                ('fin_contraro', models.DateTimeField(blank=True, max_length=8)),
                ('salario', models.PositiveIntegerField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
