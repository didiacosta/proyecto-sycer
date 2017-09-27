from django.contrib import admin

from .models import Asignacion_espacio
from acciones import export_as_excel

class AdminAsignacion_espacio(admin.ModelAdmin):
	list_display=('id_empresa','espacio','fecha_asignacion')
	search_fields=('id_empresa__nombre',)
	actions = (export_as_excel, )
	raw_id_fields = ('id_empresa',)


admin.site.register(Asignacion_espacio,AdminAsignacion_espacio)
