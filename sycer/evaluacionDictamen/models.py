from django.db import models
from dictamen.models import Dictamen
from aspectoEvaluado.models import BAspectoEvaluado
# Create your models here.
class EvaluacionDictamen(models.Model):
	respuestas = ((u'0',u'[Seleccione...]'),(u'1',u'Aplica'),
		(u'2',u'Cumple'),
		(u'3',u'No cumple'),)
	dictamen = models.ForeignKey(Dictamen)
	aspectoEvaluado = models.ForeignKey(BAspectoEvaluado)
	respuesta = models.CharField(max_length=1,choices=respuestas, default=0)

	def nombreRespuesta(self):
		retorno ='No encontrado'
		
		if self.respuesta == '1':
			retorno='No Aplica'
		if self.respuesta=='2':
			retorno = 'Cumple'
		if self.respuesta=='3':
			retorno='No cumple'
		return retorno	

	def __unicode__(self):
		return str(self.dictamen.numero) + ' - ' + self.aspectoEvaluado.nombre + ' - ' + self.nombreRespuesta() 


