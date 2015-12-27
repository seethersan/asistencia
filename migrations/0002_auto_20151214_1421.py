# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='countries_id',
            field=models.ForeignKey(default=1, verbose_name=b'Pais', to='asistencia.countries'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='departamento_id',
            field=models.ForeignKey(default=11, verbose_name=b'Departamento', to='asistencia.departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='provincia_id',
            field=models.ForeignKey(default=103, verbose_name=b'Provincia', to='asistencia.provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='countries_id',
            field=models.ForeignKey(default=1, verbose_name=b'Pais', to='asistencia.countries'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='departamento_id',
            field=models.ForeignKey(default=11, verbose_name=b'Departamento', to='asistencia.departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='direccion_name',
            field=models.CharField(default='Calle Real 1335', max_length=50, verbose_name=b'Direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='provincia_id',
            field=models.ForeignKey(default=11, verbose_name=b'Provincia', to='asistencia.provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='local',
            name='countries_id',
            field=models.ForeignKey(default=1, verbose_name=b'Pais', to='asistencia.countries'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='local',
            name='departamento_id',
            field=models.ForeignKey(default=11, verbose_name=b'Departamento', to='asistencia.departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='local',
            name='provincia_id',
            field=models.ForeignKey(default=103, verbose_name=b'Provincia', to='asistencia.provincia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='area',
            name='area_name',
            field=models.CharField(max_length=30, verbose_name=b'Area'),
        ),
        migrations.AlterField(
            model_name='area',
            name='empresa_id',
            field=models.ForeignKey(verbose_name=b'Empresa', to='asistencia.empresa'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='country_name',
            field=models.CharField(max_length=100, verbose_name=b'Pais'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='countries_id',
            field=models.ForeignKey(verbose_name=b'Pais', to='asistencia.countries'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='departamento_name',
            field=models.CharField(max_length=30, verbose_name=b'Departamento'),
        ),
        migrations.AlterField(
            model_name='distrito',
            name='distrito_name',
            field=models.CharField(max_length=70, verbose_name=b'Distrito'),
        ),
        migrations.AlterField(
            model_name='distrito',
            name='provincia_id',
            field=models.ForeignKey(verbose_name=b'Provincia', to='asistencia.provincia'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='countries_id',
            field=models.ForeignKey(verbose_name=b'Pais', to='asistencia.countries'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='documento_name',
            field=models.CharField(max_length=30, verbose_name=b'Documento'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='area_id',
            field=models.ForeignKey(verbose_name=b'Area', to='asistencia.area'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='distrito_id',
            field=models.ForeignKey(verbose_name=b'Distrito', to='asistencia.distrito'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='documento_id',
            field=models.ForeignKey(verbose_name=b'Tipo de documento', to='asistencia.documento'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='empleado_direccion',
            field=models.CharField(max_length=30, verbose_name=b'Direccion'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='empleado_nrodocumento',
            field=models.CharField(max_length=12, verbose_name=b'Numero de documento'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='empleado_telefono',
            field=models.CharField(max_length=12, verbose_name=b'Telefono'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='horario_id',
            field=models.ForeignKey(verbose_name=b'Horario', to='asistencia.horario'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='local_id',
            field=models.ForeignKey(verbose_name=b'Local', to='asistencia.local'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='user',
            field=models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='distrito_id',
            field=models.ForeignKey(verbose_name=b'Distrito', to='asistencia.distrito'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='empresa_name',
            field=models.CharField(max_length=40, verbose_name=b'Razon Social'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='empresa_ruc',
            field=models.CharField(max_length=11, verbose_name=b'RUC'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_entrada',
            field=models.TimeField(verbose_name=b'Hora de entrada'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_name',
            field=models.CharField(max_length=30, verbose_name=b'Horario'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_salida',
            field=models.TimeField(verbose_name=b'Hora de salida'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_tolerancia',
            field=models.SmallIntegerField(verbose_name=b'Tiempo de tolerancia'),
        ),
        migrations.AlterField(
            model_name='local',
            name='distrito_id',
            field=models.ForeignKey(verbose_name=b'Distrito', to='asistencia.distrito'),
        ),
        migrations.AlterField(
            model_name='local',
            name='empresa_id',
            field=models.ForeignKey(verbose_name=b'Empresa', to='asistencia.empresa'),
        ),
        migrations.AlterField(
            model_name='local',
            name='local_direccion',
            field=models.CharField(max_length=50, verbose_name=b'Direccion'),
        ),
        migrations.AlterField(
            model_name='local',
            name='local_name',
            field=models.CharField(max_length=30, verbose_name=b'Local'),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='departamento_id',
            field=models.ForeignKey(verbose_name=b'Departamento', to='asistencia.departamento'),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='provincia_name',
            field=models.CharField(max_length=70, verbose_name=b'Provincia'),
        ),
    ]
