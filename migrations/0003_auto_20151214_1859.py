# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_auto_20151214_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='countries_id',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='departamento_id',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='provincia_id',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='countries_id',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='departamento_id',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='provincia_id',
        ),
        migrations.RemoveField(
            model_name='local',
            name='countries_id',
        ),
        migrations.RemoveField(
            model_name='local',
            name='departamento_id',
        ),
        migrations.RemoveField(
            model_name='local',
            name='provincia_id',
        ),
        migrations.AddField(
            model_name='empleado',
            name='fnacimiento',
            field=models.DateField(default=0, verbose_name=b'Fecha de Nacimiento'),
            preserve_default=False,
        ),
    ]
