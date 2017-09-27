# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictamen', '0004_auto_20161118_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictamen',
            name='observaciones',
            field=models.TextField(max_length=150),
        ),
    ]
