# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20161026_0810'),
        ('municipio', '__first__'),
        ('dictamen', '0002_dictamen_aprobada'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictamen',
            name='municipio',
            field=models.ForeignKey(to='municipio.Municipio', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictamen',
            name='organismo',
            field=models.ForeignKey(to='empresa.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictamen',
            name='tipo',
            field=models.CharField(default=0, max_length=1, choices=[('1', 'Distribucion'), ('1', 'Subestacion'), ('1', 'Usuario Final')]),
            preserve_default=True,
        ),
    ]
