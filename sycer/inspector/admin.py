from django.contrib import admin

from .models import Inspector
from acciones import export_as_excel


class InspectorAdmin(admin.ModelAdmin):
	list_display =('nombres','apellidos','matricula_profesional')
	#list_filter = ('cliente__id_cliente__nombre',)
	search_fields = ('nombres','apellidos','matricula_profesional')
	actions = (export_as_excel, )

admin.site.register(Inspector,InspectorAdmin)
