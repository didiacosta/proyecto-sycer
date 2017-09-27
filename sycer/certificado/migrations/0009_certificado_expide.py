# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20161026_0810'),
        ('certificado', '0008_remove_certificado_id_empresa_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='expide',
            field=models.ForeignKey(default=1, to='empresa.Empresa'),
            preserve_default=False,
        ),
    ]
