# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0005_auto_20151214_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fnacimiento',
            field=models.DateField(default=datetime.datetime.now, null=True, verbose_name=b'Fecha de Nacimiento'),
        ),
    ]
