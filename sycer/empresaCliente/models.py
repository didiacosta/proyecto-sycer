from django.db import models
from empresa.models import Empresa
from cliente.models import Cliente
# Create your models here.

class EmpresaCliente(models.Model):
	id_empresa=models.ForeignKey(Empresa)
	id_cliente=models.ForeignKey(Cliente)

	def __unicode__(self):
		return self.id_empresa.nombre + ' [' + self.id_cliente.nombre + ']'
