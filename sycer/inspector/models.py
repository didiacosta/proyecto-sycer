from django.db import models

# Create your models here.
class Inspector(models.Model):
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	matricula_profesional = models.CharField(max_length=50, unique=True)
	activo = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombres + ' ' + self.apellidos 
