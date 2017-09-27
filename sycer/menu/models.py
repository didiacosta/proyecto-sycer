from django.db import models

from aplicacion.models import Aplicacion
# Create your models here.
class Menu (models.Model):
	label=models.CharField(max_length=30)
	destino=models.CharField(max_length=50)
	icono=models.CharField(max_length=50)
	padre=models.PositiveIntegerField()
	orden=models.PositiveIntegerField()
	id_aplicacion=models.ForeignKey(Aplicacion)

	def __unicode__(self):
		return self.label
