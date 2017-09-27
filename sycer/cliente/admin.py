from django.contrib import admin

from .models import Cliente
from acciones import export_as_excel

class AdminCliente(admin.ModelAdmin):
	list_display=('nombre','nit','activo')
	list_filter=('estado',)
	search_fields=('nombre','nit')
	actions = (export_as_excel, )

	def activo(self,obj):
		return obj.estado == 1

	activo.boolean = True

admin.site.register(Cliente,AdminCliente)
