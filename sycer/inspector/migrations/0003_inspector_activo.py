# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspector', '0002_auto_20161120_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspector',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
