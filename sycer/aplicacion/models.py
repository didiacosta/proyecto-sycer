from django.db import models

# Create your models here.
class Aplicacion (models.Model):
	nombre=models.CharField(max_length=50)
	icono=models.CharField(max_length=40)

	def __unicode__(self):
		return self.nombre