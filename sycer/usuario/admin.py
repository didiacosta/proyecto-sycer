from django.contrib import admin

from .models import Usuario
from django.conf import settings
from acciones import export_as_excel

class AdminUsuario(admin.ModelAdmin):
	list_display=('nombres','apellidos','telefono','id_empresa','es_administrador', 'foto_usuario')
	list_filter=('id_empresa','administrador')
	#search_fields=('first_name','last_name')
	actions = (export_as_excel, )
	raw_id_fields = ('id_empresa',)

	def es_administrador(self,obj):
		return obj.administrador == 1

	es_administrador.boolean = True

admin.site.register(Usuario, AdminUsuario)
