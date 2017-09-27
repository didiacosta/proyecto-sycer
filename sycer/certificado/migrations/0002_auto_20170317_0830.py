# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificado',
            name='codigoSeguridad',
        ),
        migrations.RemoveField(
            model_name='certificado',
            name='observacion',
        ),
        migrations.RemoveField(
            model_name='certificado',
            name='pesoArchivo',
        ),
        migrations.RemoveField(
            model_name='certificado',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='certificado',
            name='id_empresa_cliente',
            field=models.ForeignKey(to='empresaCliente.EmpresaCliente'),
        ),
    ]
