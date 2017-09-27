# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresaCliente', '__first__'),
        ('inspector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('anexos', models.CharField(max_length=150)),
                ('observaciones', models.CharField(max_length=150)),
                ('cliente', models.ForeignKey(to='empresaCliente.EmpresaCliente')),
                ('director_tecnico', models.ForeignKey(related_name=b'director_tecnico', to='inspector.Inspector')),
                ('inspector', models.ForeignKey(related_name=b'inspector_tecnico', to='inspector.Inspector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
