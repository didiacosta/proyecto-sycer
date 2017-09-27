from django.conf.urls import patterns,url

from empresaCliente.views import EmpresaClienteListView,EmpresaClienteDetailView, EmpresaClienteUpdateView, EmpresaClienteCreateView, EmpresaClienteDeleteView, generar_pdf
#from empresaCliente.views import views
urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
    url(r'^clientes/$', EmpresaClienteListView.as_view(), name='empresaCliente.empresaCLiente-list'),
    url(r'^editarCliente/(?P<pk>[\w\-]+)/$', EmpresaClienteUpdateView.as_view(), name='empresaCliente.editarEmpresaCliente'),
    url(r'^crearCliente/$', EmpresaClienteCreateView.as_view(), name='empresaCliente.crearEmpresaCliente'),
    url(r'^borrarCliente/(?P<pk>[\w\-]+)/$', EmpresaClienteDeleteView.as_view(), name='empresaCliente.borrarEmpresaCliente'),
    url(r'^clientes-reporte/$', generar_pdf, name='empresaCliente.empresaCLiente-reporte'),
]