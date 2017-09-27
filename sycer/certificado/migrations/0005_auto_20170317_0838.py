# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificado', '0004_auto_20170317_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='id_empresa_cliente',
            field=models.ForeignKey(verbose_name=b'Cliente', to='empresaCliente.EmpresaCliente'),
        ),
    ]
