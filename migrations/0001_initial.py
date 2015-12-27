# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('area_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('country_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('departamento_name', models.CharField(max_length=30)),
                ('countries_id', models.ForeignKey(to='asistencia.countries')),
            ],
        ),
        migrations.CreateModel(
            name='distrito',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('distrito_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='documento',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('documento_name', models.CharField(max_length=30)),
                ('countries_id', models.ForeignKey(to='asistencia.countries')),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('empleado_direccion', models.CharField(max_length=30)),
                ('empleado_telefono', models.CharField(max_length=12)),
                ('empleado_nrodocumento', models.CharField(max_length=12)),
                ('area_id', models.ForeignKey(to='asistencia.area')),
                ('distrito_id', models.ForeignKey(to='asistencia.distrito')),
                ('documento_id', models.ForeignKey(to='asistencia.documento')),
            ],
        ),
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('empresa_ruc', models.CharField(max_length=11)),
                ('empresa_name', models.CharField(max_length=40)),
                ('distrito_id', models.ForeignKey(to='asistencia.distrito')),
            ],
        ),
        migrations.CreateModel(
            name='horario',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('horario_name', models.CharField(max_length=30)),
                ('horario_entrada', models.TimeField()),
                ('horario_salida', models.TimeField()),
                ('horario_tolerancia', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='local',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('local_name', models.CharField(max_length=30)),
                ('local_direccion', models.CharField(max_length=50)),
                ('distrito_id', models.ForeignKey(to='asistencia.distrito')),
                ('empresa_id', models.ForeignKey(to='asistencia.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='provincia',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('provincia_name', models.CharField(max_length=70)),
                ('departamento_id', models.ForeignKey(to='asistencia.departamento')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='horario_id',
            field=models.ForeignKey(to='asistencia.horario'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='local_id',
            field=models.ForeignKey(to='asistencia.local'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia_id',
            field=models.ForeignKey(to='asistencia.provincia'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='empleado_id',
            field=models.ForeignKey(to='asistencia.empleado'),
        ),
        migrations.AddField(
            model_name='area',
            name='empresa_id',
            field=models.ForeignKey(to='asistencia.empresa'),
        ),
    ]
