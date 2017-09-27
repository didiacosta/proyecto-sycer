from django.contrib import admin

from .models import AccesoAccion
from acciones import export_as_excel

class AdminAccesoAccion(admin.ModelAdmin):
	list_display=('idAcceso','idAccion','activa')
	list_filter=('activa',)
	search_fields=('idAcceso__id_usuario__nombres','idAcceso__id_aplicacion__nombre')
	list_editable=('activa',)
	actions = (export_as_excel, )
	raw_id_fields = ('idAcceso','idAccion',)



admin.site.register(AccesoAccion,AdminAccesoAccion)
