# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictamen', '0003_auto_20161118_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictamen',
            name='matriculaInterventoria',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictamen',
            name='matriculaResponsableContruccion',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictamen',
            name='matriculaResponsableDiseno',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictamen',
            name='responsableContruccion',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictamen',
            name='responsableDiseno',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictamen',
            name='responsableInterventoria',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dictamen',
            name='tipo',
            field=models.CharField(default=0, max_length=1, choices=[('0', '[Seleccione...]'), ('1', 'Distribucion'), ('2', 'Subestacion'), ('3', 'Usuario Final')]),
        ),
    ]
