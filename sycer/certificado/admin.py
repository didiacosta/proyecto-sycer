from django.contrib import admin

from .models import Certificado
from acciones import export_as_excel

class AdminCertificado(admin.ModelAdmin):
	list_display=('expide','nombre','tipo','pesoArchivo', 'archivo','numero','codigoSeguridad')
	list_filter=('tipo','expide')
	search_fields=('nombre','descripcion')
	actions = (export_as_excel, )
	raw_id_fields = ('tipo',)

admin.site.register(Certificado,AdminCertificado)
