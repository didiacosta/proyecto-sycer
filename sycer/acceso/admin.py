from django.contrib import admin

from .models import Acceso
from acciones import export_as_excel

class AdminAcceso(admin.ModelAdmin):
	list_display=('id_usuario','id_aplicacion')
	list_filter=('id_aplicacion',)
	search_fields=('id_usuario__nombres','id_usuario__apellidos')
	actions = (export_as_excel, )
	raw_id_fields = ('id_usuario','id_aplicacion',)

admin.site.register(Acceso,AdminAcceso)
