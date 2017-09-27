from django.db import models
from dictamen.models import Dictamen
from municipio.models import Municipio
# Create your models here.
class DictamenDistribucionInstalacion(models.Model):
	dictamen = models.ForeignKey(Dictamen, null=False)
	localizacion = models.ForeignKey(Municipio, null=False)
	tension = models.FloatField()
	capacidad = models.FloatField()
	zona = models.CharField(max_length=1,choices=((u'0',u'[Seleccione...]'),(u'1',u'Urbano'),
		(u'2',u'Rural'),
		(u'3',u'Aislada'),), default=0)
	servicio = models.CharField(max_length=1,choices=((u'0',u'[Seleccione...]'),(u'1',u'Residencial'),
		(u'2',u'Comercial'),
		(u'3',u'Industrial'),), default=0)
	uso = models.CharField(max_length=1,choices=((u'0',u'[Seleccione...]'),(u'1',u'General'),
		(u'2',u'Exclusivo'),
		(u'3',u'Alumbrado publico'),
		(u'3',u'Uso final'),), default=0)
	configuracion=models.CharField(max_length=1,choices=((u'0',u'[Seleccione...]'),(u'1',u'Monofasica'),
		(u'2',u'Trifasica'),), default=0)

	longitud = models.FloatField()
	tipoYcalibreCondutor=models.CharField(max_length=20,null=True)
	materialEstructura=models.CharField(max_length=50,null=True)
	cantidadEstructuras = models.IntegerField()
	anoTerminacion=models.IntegerField()

	def __unicode__(self):
		return self.dictamen.numero + '[' + self.localizacion + ']'



