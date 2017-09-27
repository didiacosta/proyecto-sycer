from django.conf.urls import patterns,url

from dictamen.views import DictamenListView, DictamenCreateView, DictamenUpdateView, DictamenDetailView
#, EmpresaInspectorDeleteView#, generar_pdf
from evaluacionDictamen.views import guardarEvaluacion
urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
    url(r'^dictamenes/$', DictamenListView.as_view(), name='dictamen.dictamen-list'),
    url(r'^editarDictamen/(?P<pk>[\w\-]+)/$', DictamenUpdateView.as_view(), name='dictamen.editarDictamen'),
    url(r'^crearDictamen/$', DictamenCreateView.as_view(), name='dictamen.crearDictamen'),
    url(r'^detalleDictamen/(?P<idDictamen>[\w\-]+)/$', DictamenDetailView.as_view(), name='Dictamen.Dictamen-detalle'),
    url(r'^guardarEvaluacion/$', guardarEvaluacion, name='dictamen.guardarEvaluacion'),
    # url(r'^borrarInspector/(?P<pk>[\w\-]+)/$', EmpresaInspectorDeleteView.as_view(), name='empresaInspector.borrarEmpresaInspector'),
    # url(r'^Inspectors-reporte/$', generar_pdf, name='empresaInspector.empresaInspector-reporte'),
]