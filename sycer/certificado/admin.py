from django.contrib import admin

from .models import Certificado
from acciones import export_as_excel

class AdminCertificado(admin.ModelAdmin):
	list_display=('id_empresa_cliente','nombre','tipo','pesoArchivo', 'archivo')
	list_filter=('id_empresa_cliente__id_empresa__nombre','tipo')
	search_fields=('nombre','descripcion')
	actions = (export_as_excel, )
	raw_id_fields = ('id_empresa_cliente','tipo',)

admin.site.register(Certificado,AdminCertificado)
