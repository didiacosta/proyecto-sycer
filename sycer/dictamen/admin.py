from django.contrib import admin

from .models import Dictamen
from acciones import export_as_excel

from dictamen.models import Dictamen

#class UsuarioInline(admin.StackedInLine):
#	model = Usuario
#	extra = 1

class DictamenAdmin(admin.ModelAdmin):
	list_display =('nombreCliente','numero')
	list_filter = ('cliente__id_cliente__nombre',)
	search_fields = ('numero','inspector__nombres','inspector__apellidos')
	actions = (export_as_excel, )

admin.site.register(Dictamen,DictamenAdmin)

