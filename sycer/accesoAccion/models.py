from django.db import models
from acceso.models import Acceso
from accion.models import Accion
# Create your models here.
class AccesoAccion (models.Model):
	idAcceso = models.ForeignKey(Acceso)
	idAccion = models.ForeignKey(Accion)
	activa = models.PositiveIntegerField()

	#acciones = models.ManyToManyField('acceso.Acceso',blank=True)

	def __unicode__(self):
		return self.idAcceso.id_usuario.nombres + ' ' + self.idAcceso.id_usuario.apellidos + ' (' + self.idAcceso.id_aplicacion.nombre + ')[' + self.idAccion.nombre + ']'