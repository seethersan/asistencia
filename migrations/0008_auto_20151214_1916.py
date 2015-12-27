# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0007_auto_20151214_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fnacimiento',
            field=models.DateField(null=True, verbose_name=b'Fecha de Nacimiento'),
        ),
    ]
