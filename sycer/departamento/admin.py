from django.contrib import admin

# Register your models here.
from .models import Departamento
from acciones import export_as_excel

class DepartamentoAdmin(admin.ModelAdmin):
	list_display =('nombre',)
	search_fields = ('nombre',)
	actions = (export_as_excel, )

admin.site.register(Departamento,DepartamentoAdmin)