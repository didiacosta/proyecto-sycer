from django.db import models
from empresa.models import Empresa
class Asignacion_espacio(models.Model):
	id_empresa = models.ForeignKey(Empresa)
	espacio = models.PositiveIntegerField(null = False)
	fecha_asignacion = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.id_empresa.nombre + '[' + str(self.fecha_asignacion) + ']'