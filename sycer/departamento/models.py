from django.db import models

# Create your models here.
class Departamento(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre
