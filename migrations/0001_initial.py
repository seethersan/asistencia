# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_name', models.CharField(max_length=30, verbose_name=b'Area')),
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
                ('country_name', models.CharField(max_length=100, verbose_name=b'Pais')),
            ],
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('departamento_name', models.CharField(max_length=30, verbose_name=b'Departamento')),
                ('countries_id', models.ForeignKey(verbose_name=b'Pais', to='asistencia.countries')),
            ],
        ),
        migrations.CreateModel(
            name='distrito',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('distrito_name', models.CharField(max_length=70, verbose_name=b'Distrito')),
            ],
        ),
        migrations.CreateModel(
            name='documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento_name', models.CharField(max_length=30, verbose_name=b'Documento')),
                ('countries_id', models.ForeignKey(verbose_name=b'Pais', to='asistencia.countries')),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.CharField(max_length=10, serialize=False, verbose_name=b'C\xc3\xb3digo', primary_key=True)),
                ('empleado_direccion', models.CharField(max_length=30, verbose_name=b'Direccion')),
                ('empleado_telefono', models.CharField(max_length=12, verbose_name=b'Telefono')),
                ('empleado_nrodocumento', models.CharField(max_length=12, verbose_name=b'Numero de documento')),
                ('area_id', models.ForeignKey(verbose_name=b'Area', to='asistencia.area')),
                ('distrito_id', models.ForeignKey(verbose_name=b'Distrito', to='asistencia.distrito')),
                ('documento_id', models.ForeignKey(verbose_name=b'Tipo de documento', to='asistencia.documento')),
            ],
        ),
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empresa_ruc', models.CharField(max_length=11, verbose_name=b'RUC')),
                ('empresa_name', models.CharField(max_length=40, verbose_name=b'Razon Social')),
                ('direccion_name', models.CharField(max_length=50, verbose_name=b'Direccion')),
                ('distrito_id', models.ForeignKey(verbose_name=b'Distrito', to='asistencia.distrito')),
            ],
        ),
        migrations.CreateModel(
            name='horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario_name', models.CharField(max_length=30, verbose_name=b'Horario')),
                ('horario_entrada', models.TimeField(verbose_name=b'Hora de entrada')),
                ('horario_salida', models.TimeField(verbose_name=b'Hora de salida')),
                ('horario_tolerancia', models.SmallIntegerField(verbose_name=b'Tiempo de tolerancia')),
            ],
        ),
        migrations.CreateModel(
            name='local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('local_name', models.CharField(max_length=30, verbose_name=b'Local')),
                ('local_direccion', models.CharField(max_length=50, verbose_name=b'Direccion')),
                ('distrito_id', models.ForeignKey(verbose_name=b'Distrito', to='asistencia.distrito')),
                ('empresa_id', models.ForeignKey(verbose_name=b'Empresa', to='asistencia.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='provincia',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('provincia_name', models.CharField(max_length=70, verbose_name=b'Provincia')),
                ('departamento_id', models.ForeignKey(verbose_name=b'Departamento', to='asistencia.departamento')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='horario_id',
            field=models.ForeignKey(verbose_name=b'Horario', to='asistencia.horario'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='local_id',
            field=models.ForeignKey(verbose_name=b'Local', to='asistencia.local'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia_id',
            field=models.ForeignKey(verbose_name=b'Provincia', to='asistencia.provincia'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='empleado_id',
            field=models.ForeignKey(to='asistencia.empleado'),
        ),
        migrations.AddField(
            model_name='area',
            name='empresa_id',
            field=models.ForeignKey(verbose_name=b'Empresa', to='asistencia.empresa'),
        ),
    ]
