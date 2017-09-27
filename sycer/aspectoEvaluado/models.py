from django.db import models

# Create your models here.
# Create your models here.
class BaseModel(models.Model):
	orden = models.IntegerField(default=1)
	nombre = models.CharField(max_length=500)

	class Meta:
		abstract = True

	def __unicode__(self):
		return self.nombre

class ARequisitoEsencial(BaseModel):
	tipoDictamen = ((u'0',u'[Seleccione...]'),(u'1',u'Distribucion'),
		(u'2',u'Subestacion'),
		(u'3',u'Usuario Final'),)
	tipo = models.CharField(max_length=1,choices=tipoDictamen, default=0)	
	class Meta:
		db_table = 'requisitoEsencial'

	def nombreTipo(self):
		retorno ='No encontrado'
		
		if self.tipo == '1':
			retorno='Distribucion'
		if self.tipo=='2':
			retorno = 'Subestacion'
		if self.tipo=='3':
			retorno='Usuario Final'
		return retorno

	def __unicode__(self):
		return  self.nombreTipo() + ' - ' + self.nombre



class BAspectoEvaluado(BaseModel):
	requisitoEsencial = models.ForeignKey(ARequisitoEsencial, null=False)
	class Meta:
		db_table = 'aspectoEvaluado'

	def __unicode__(self):
		return self.requisitoEsencial.nombreTipo() + ' - ' +self.requisitoEsencial.nombre + ' - ' + self.nombre
