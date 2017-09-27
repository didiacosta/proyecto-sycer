from django.db import models
from tipoCertificado.models import TipoCertificado
from empresaCliente.models import EmpresaCliente
from municipio.models import Municipio
# Create your models here.
class Certificado(models.Model):
	id_empresa_cliente=models.ForeignKey(EmpresaCliente, verbose_name='Cliente')
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=100, null=True, blank=True)
	ruta = models.FileField(upload_to='soporte/')
	observacion = models.TextField(max_length=100, null=True, blank=True)
	tipo=models.ForeignKey(TipoCertificado, verbose_name='Tipo de certificado')
	pesoArchivo = models.PositiveIntegerField(default=0, verbose_name='Peso del archivo')
	fecha = models.DateField()
	numero = models.CharField(max_length=50)
	codigoSeguridad= models.CharField(max_length=50, verbose_name='Codigo de seguridad')
	municipio = models.ForeignKey(Municipio)
	# id_empresa_cliente=models.ForeignKey(EmpresaCliente)
	# nombre = models.CharField(max_length=50)
	# descripcion = models.CharField(max_length=100)
	# ruta = models.FileField(upload_to='soporte/')
	# observacion = models.CharField(max_length=100)
	# tipo=models.ForeignKey(TipoCertificado)
	# pesoArchivo = models.PositiveIntegerField()
	# fecha = models.DateField()
	# numero = models.CharField(max_length=50)
	# municipio = models.ForeignKey(Municipio)

	def archivo(self):
		return """<a href="%s">archivo</a> """ % self.ruta.url

	archivo.allow_tags=True

	def __unicode__(self):
		return self.id_empresa_cliente.id_empresa.nombre + ' (' + self.tipo.nombre  + ')'+' [' + self.nombre + ']' 