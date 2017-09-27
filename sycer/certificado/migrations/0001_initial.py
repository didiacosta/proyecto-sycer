# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresaCliente', '__first__'),
        ('municipio', '__first__'),
        ('tipoCertificado', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('ruta', models.FileField(upload_to=b'soporte/')),
                ('observacion', models.TextField(max_length=100)),
                ('pesoArchivo', models.PositiveIntegerField(default=0, verbose_name=b'Peso del archivo')),
                ('fecha', models.DateField()),
                ('numero', models.CharField(max_length=50)),
                ('codigoSeguridad', models.CharField(max_length=50, verbose_name=b'Codigo de seguridad')),
                ('id_empresa_cliente', models.ForeignKey(verbose_name=b'Cliente', to='empresaCliente.EmpresaCliente')),
                ('municipio', models.ForeignKey(to='municipio.Municipio')),
                ('tipo', models.ForeignKey(verbose_name=b'Tipo de certificado', to='tipoCertificado.TipoCertificado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
