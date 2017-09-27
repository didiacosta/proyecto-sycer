# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificado', '0003_auto_20170317_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='codigoSeguridad',
            field=models.CharField(default=0, max_length=50, verbose_name=b'Codigo de seguridad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificado',
            name='observacion',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='pesoArchivo',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Peso del archivo'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='tipo',
            field=models.ForeignKey(verbose_name=b'Tipo de certificado', to='tipoCertificado.TipoCertificado'),
        ),
    ]
