# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aspectoEvaluado', '0002_arequisitoesencial_tipo'),
        ('dictamen', '0004_auto_20161118_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionDictamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(default=0, max_length=1, choices=[('0', '[Seleccione...]'), ('1', 'Aplica'), ('2', 'Cumple'), ('3', 'No cumple')])),
                ('aspectoEvaluado', models.ForeignKey(to='aspectoEvaluado.BAspectoEvaluado')),
                ('dictamen', models.ForeignKey(to='dictamen.Dictamen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
