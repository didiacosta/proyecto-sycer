# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificado', '0005_auto_20170317_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='descripcion',
            field=models.TextField(max_length=100),
        ),
    ]
