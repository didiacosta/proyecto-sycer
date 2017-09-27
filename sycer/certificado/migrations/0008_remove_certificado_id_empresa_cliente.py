# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificado', '0007_auto_20170317_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificado',
            name='id_empresa_cliente',
        ),
    ]
