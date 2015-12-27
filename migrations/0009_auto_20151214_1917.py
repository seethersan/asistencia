# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0008_auto_20151214_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fnacimiento',
            field=models.DateField(default=datetime.date(2015, 12, 14), null=True, verbose_name=b'Fecha de Nacimiento'),
        ),
    ]
