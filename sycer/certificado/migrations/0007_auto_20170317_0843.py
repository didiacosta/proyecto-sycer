# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificado', '0006_auto_20170317_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='descripcion',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='observacion',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
