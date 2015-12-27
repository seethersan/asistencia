# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0009_auto_20151214_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='fnacimiento',
        ),
    ]
