from django.db import models
from aplicacion.models import Aplicacion
from usuario.models import Usuario
# Create your models here.
class Acceso (models.Model):
	id_usuario=models.ForeignKey(Usuario)
	id_aplicacion=models.ForeignKey(Aplicacion)

	def __unicode__(self):
		return self.id_usuario.nombres + ' ' + self.id_usuario.apellidos + ' (' + self.id_aplicacion.nombre + ')'