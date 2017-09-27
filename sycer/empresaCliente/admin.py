from django.contrib import admin

from .models import EmpresaCliente
from acciones import export_as_excel

class AdminEmpresaCliente(admin.ModelAdmin):
	list_display=('id_empresa','id_cliente')
	list_filter = ('id_empresa',)
	search_fields=('id_cliente__nombre','id_empresa__nombre')
	actions = (export_as_excel, )
	raw_id_fields = ('id_empresa','id_cliente')

admin.site.register(EmpresaCliente,AdminEmpresaCliente)
