from django.contrib import admin

from .models import Empresa
from acciones import export_as_excel

from usuario.models import Usuario

#class UsuarioInline(admin.StackedInLine):
#	model = Usuario
#	extra = 1

class EmpresaAdmin(admin.ModelAdmin):
	list_display =('nombre','nit','logo_Empresa','resolucion','direccion','telefono','activo')
	list_filter = ('nombre','estado')
	search_fields = ('nombre',)
	actions = (export_as_excel, )
#	inlines = [UsuarioInline,]

	def activo(self,obj):
		return obj.estado == 1

	activo.boolean = True

admin.site.register(Empresa,EmpresaAdmin)
