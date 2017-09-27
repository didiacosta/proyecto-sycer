# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20161026_0810'),
        ('inspector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaInspector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empresa', models.ForeignKey(to='empresa.Empresa')),
                ('inspector', models.ForeignKey(to='inspector.Inspector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
