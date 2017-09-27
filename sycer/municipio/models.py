from django.db import models
from departamento.models import Departamento
# Create your models here.
class Municipio(models.Model):
	departamento = models.ForeignKey(Departamento)
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre + ' - ' + self.departamento.nombre

