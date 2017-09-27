from django.db import models
from empresaCliente.models import EmpresaCliente
from empresa.models import Empresa
from inspector.models import Inspector
from municipio.models import Municipio

# Create your models here.
class Dictamen(models.Model):
	tipoDictamen = ((u'0',u'[Seleccione...]'),(u'1',u'Distribucion'),
		(u'2',u'Subestacion'),
		(u'3',u'Usuario Final'),)
	cliente = models.ForeignKey(EmpresaCliente)
	numero = models.IntegerField()
	inspector = models.ForeignKey(Inspector, related_name='inspector_tecnico')
	director_tecnico = models.ForeignKey(Inspector, related_name='director_tecnico')
	anexos = models.CharField(max_length=150)
	observaciones = models.TextField(max_length=150)
	aprobada = models.BooleanField(default=False)
	municipio = models.ForeignKey(Municipio, null=True)
	organismo = models.ForeignKey(Empresa, null=True)
	tipo = models.CharField(max_length=1,choices=tipoDictamen, default=0)
	responsableDiseno = models.CharField(max_length=100, null=True)
	matriculaResponsableDiseno = models.CharField(max_length=100, null=True)
	responsableInterventoria = models.CharField(max_length=100, null=True)
	matriculaInterventoria = models.CharField(max_length=100, null=True)
	responsableContruccion = models.CharField(max_length=100, null=True)
	matriculaResponsableContruccion = models.CharField(max_length=100, null=True)

	def nombreTipo(self):
		retorno ='No encontrado'
		
		if self.tipo == '1':
			retorno='Distribucion'
		if self.tipo=='2':
			retorno = 'Subestacion'
		if self.tipo=='3':
			retorno='Usuario Final'
		return retorno
		
	def nombreCliente(self):
		return self.cliente.id_cliente.nombre

	def __unicode__(self):
		return self.cliente.id_cliente.nombre + ' - ' + str(self.numero)
