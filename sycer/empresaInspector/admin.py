from django.contrib import admin

from .models import EmpresaInspector
from acciones import export_as_excel

class AdminEmpresaInspector(admin.ModelAdmin):
	list_display=('empresa','inspector')
	list_filter = ('empresa',)
	search_fields=('inspector__nombres','inspector__apellidos')
	actions = (export_as_excel, )
	

admin.site.register(EmpresaInspector,AdminEmpresaInspector)
