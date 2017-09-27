# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipoCertificado', '__first__'),
        ('certificado', '0002_auto_20170317_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='observacion',
            field=models.CharField(default='hola', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificado',
            name='pesoArchivo',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificado',
            name='tipo',
            field=models.ForeignKey(default=1, to='tipoCertificado.TipoCertificado'),
            preserve_default=False,
        ),
    ]
