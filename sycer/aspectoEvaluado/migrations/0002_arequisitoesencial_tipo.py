# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aspectoEvaluado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arequisitoesencial',
            name='tipo',
            field=models.CharField(default=0, max_length=1, choices=[('0', '[Seleccione...]'), ('1', 'Distribucion'), ('2', 'Subestacion'), ('3', 'Usuario Final')]),
            preserve_default=True,
        ),
    ]
