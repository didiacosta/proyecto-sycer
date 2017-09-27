from django.contrib import admin
from .models import ARequisitoEsencial, BAspectoEvaluado
from acciones import export_as_excel

# Register your models here.
class ARequisitoEsencialAdmin(admin.ModelAdmin):
	list_display =('nombre','orden','nombreTipo')
	list_filter = ('tipo',)
	search_fields = ('nombre',)
	actions = (export_as_excel, )

admin.site.register(ARequisitoEsencial,ARequisitoEsencialAdmin)

class BAspectoEvaluadoAdmin(admin.ModelAdmin):
	list_display =('nombre','orden','requisitoEsencial')
	list_filter = ('requisitoEsencial__tipo','requisitoEsencial__nombre',)
	search_fields = ('nombre',)
	actions = (export_as_excel, )

admin.site.register(BAspectoEvaluado,BAspectoEvaluadoAdmin)