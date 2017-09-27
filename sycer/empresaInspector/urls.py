from django.conf.urls import patterns,url

from empresaInspector.views import EmpresaInspectorListView, EmpresaInspectorCreateView, EmpresaInspectorUpdateView, EmpresaInspectorDeleteView#, generar_pdf
#from empresaInspector.views import views
urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
    url(r'^Inspectores/$', EmpresaInspectorListView.as_view(), name='empresaInspector.empresaInspector-list'),
    url(r'^editarInspector/(?P<pk>[\w\-]+)/$', EmpresaInspectorUpdateView.as_view(), name='empresaInspector.editarEmpresaInspector'),
    url(r'^crearInspector/$', EmpresaInspectorCreateView.as_view(), name='empresaInspector.crearEmpresaInspector'),
    url(r'^borrarInspector/(?P<pk>[\w\-]+)/$', EmpresaInspectorDeleteView.as_view(), name='empresaInspector.borrarEmpresaInspector'),
    # url(r'^Inspectors-reporte/$', generar_pdf, name='empresaInspector.empresaInspector-reporte'),
]