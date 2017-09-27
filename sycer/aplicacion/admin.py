from django.contrib import admin

from .models import Aplicacion
from acciones import export_as_excel

class AdminAplicacion(admin.ModelAdmin):
	list_display=('nombre','icono')
	search_fields=('nombre','icono',)
	actions = (export_as_excel, )

admin.site.register(Aplicacion, AdminAplicacion)
