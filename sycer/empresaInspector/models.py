from django.db import models
from empresa.models import Empresa
from inspector.models import Inspector
# Create your models here.
class EmpresaInspector(models.Model):
	empresa=models.ForeignKey(Empresa)
	inspector=models.ForeignKey(Inspector)

	def __unicode__(self):
		return self.empresa.nombre + ' [' + self.inspector.nombres + ' ' + self.inspector.apellidos + ']' 
