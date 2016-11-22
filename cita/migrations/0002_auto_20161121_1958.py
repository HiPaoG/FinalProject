# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='pacientes',
        ),
        migrations.AddField(
            model_name='cita',
            name='fecha',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='hora',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='observaciones',
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
    ]
