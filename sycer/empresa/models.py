from django.db import models

# Create your models here.
class Empresa(models.Model):
	nombre=models.CharField(max_length=255)
	nit=models.CharField(max_length=20)
	logo=models.ImageField(upload_to='empresa')
	estado=models.PositiveIntegerField(default=1)
	resolucion = models.CharField(max_length=50, null=True)
	direccion = models.CharField(max_length=100, null=True)
	telefono = models.CharField(max_length=50, null=True)
	

	def logo_Empresa(self):
		return """<img width="100px" height="30px" src="%s" alt="logo de la empresa">""" % self.logo.url

	logo_Empresa.allow_tags=True

	logo_Empresa.admin_order_field = ('logo')	

	def __unicode__(self):
		return self.nombre

