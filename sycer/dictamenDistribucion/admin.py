from django.contrib import admin

from .models import DictamenDistribucionInstalacion
from acciones import export_as_excel


#class UsuarioInline(admin.StackedInLine):
#	model = Usuario
#	extra = 1

class DictamenDistribucionInstalacionAdmin(admin.ModelAdmin):
	list_display =('dictamen','localizacion')
	list_filter = ('dictamen',)
	search_fields = ('dictamen','localizacion')
	actions = (export_as_excel, )

admin.site.register(DictamenDistribucionInstalacion,DictamenDistribucionInstalacionAdmin)
