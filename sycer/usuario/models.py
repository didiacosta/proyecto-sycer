from django.db import models
from empresa.models import Empresa
from django.conf import settings
# Create your models here.
class Usuario(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	#correo=models.EmailField(unique = True, null = False)
	#clave=models.CharField(null = False, max_length=100)
	#nombres=models.CharField(null = False, max_length=100)
	#apellidos=models.CharField(null = False, max_length=100)
	telefono=models.CharField(null=True, max_length=100)
	foto= models.ImageField(upload_to='usuario')
	id_empresa = models.ForeignKey(Empresa)
	administrador = models.PositiveIntegerField(default = 0)

	def foto_usuario(self):
		return """<img width="100px" height="120px" src="%s" alt="foto del usuario">""" % self.foto.url

	foto_usuario.allow_tags=True

	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name

	def nombres (self):
		return self.user.first_name

	def apellidos(self):
		return self.user.last_name	



