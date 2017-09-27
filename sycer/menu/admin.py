from django.contrib import admin

from .models import Menu
from acciones import export_as_excel


class AdminMenu(admin.ModelAdmin):
	list_display=('label','destino','icono','padre','orden','id_aplicacion')
	search_fields=('label',)
	actions = (export_as_excel, )
	raw_id_fields = ('id_aplicacion',)

admin.site.register(Menu,AdminMenu)
