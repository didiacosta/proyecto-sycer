# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ARequisitoEsencial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField(default=1)),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'requisitoEsencial',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BAspectoEvaluado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField(default=1)),
                ('nombre', models.CharField(max_length=500)),
                ('requisitoEsencial', models.ForeignKey(to='aspectoEvaluado.ARequisitoEsencial')),
            ],
            options={
                'db_table': 'aspectoEvaluado',
            },
            bases=(models.Model,),
        ),
    ]
