from django.contrib import admin
from .models import EvaluacionDictamen
#from dictamen.models import Dictamen
from acciones import export_as_excel
# Register your models here.
class EvaluacionDictamenAdmin(admin.ModelAdmin):
	list_display =('dictamen','aspectoEvaluado','nombreRespuesta')
	list_filter = ('dictamen',)
	actions = (export_as_excel, )

admin.site.register(EvaluacionDictamen,EvaluacionDictamenAdmin)	
