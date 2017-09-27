# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '__first__'),
        ('dictamen', '0004_auto_20161118_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictamenDistribucionInstalacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tension', models.FloatField()),
                ('capacidad', models.FloatField()),
                ('zona', models.CharField(default=0, max_length=1, choices=[('0', '[Seleccione...]'), ('1', 'Urbano'), ('2', 'Rural'), ('3', 'Aislada')])),
                ('servicio', models.CharField(default=0, max_length=1, choices=[('0', '[Seleccione...]'), ('1', 'Residencial'), ('2', 'Comercial'), ('3', 'Industrial')])),
                ('uso', models.CharField(default=0, max_length=1, choices=[('0', '[Seleccione...]'), ('1', 'General'), ('2', 'Exclusivo'), ('3', 'Alumbrado publico'), ('3', 'Uso final')])),
                ('configuracion', models.CharField(default=0, max_length=1, choices=[('0', '[Seleccione...]'), ('1', 'Monofasica'), ('2', 'Trifasica')])),
                ('longitud', models.FloatField()),
                ('tipoYcalibreCondutor', models.CharField(max_length=20, null=True)),
                ('materialEstructura', models.CharField(max_length=50, null=True)),
                ('cantidadEstructuras', models.IntegerField()),
                ('anoTerminacion', models.IntegerField()),
                ('dictamen', models.ForeignKey(to='dictamen.Dictamen')),
                ('localizacion', models.ForeignKey(to='municipio.Municipio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
