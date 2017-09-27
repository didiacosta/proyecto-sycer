from django.contrib import admin

# Register your models here.
from .models import Municipio
from acciones import export_as_excel

class MunicipioAdmin(admin.ModelAdmin):
	list_display =('nombre',)
	list_filter=('departamento',)
	search_fields = ('nombre','departamento',)
	actions = (export_as_excel, )

admin.site.register(Municipio,MunicipioAdmin)
