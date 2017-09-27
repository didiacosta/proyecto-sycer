from django.conf.urls import patterns,url

from empresa.views import EmpresaDetailView, EmpresaUpdateView#, EmpresaCreateView, EmpresaDeleteView, EmpresaDetailView, EmpresaPublicDetailView
#from . import views

urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
   #url(r'^$', views.BusquedaEmpresaInicio_view, name='Empresa.index'),
   # url(r'^Empresas/$', EmpresaListView.as_view(), name='Empresa.Empresa-list'),
   # url(r'^crearEmpresa/$', EmpresaCreateView.as_view(), name='Empresa.Empresa-crear'),
   url(r'^editarEmpresa/(?P<pk>[\w\-]+)/$', EmpresaUpdateView.as_view(), name='Empresa.Empresa-editar'),
   # url(r'^borrarEmpresa/(?P<pk>[\w\-]+)/$', EmpresaDeleteView.as_view(), name='Empresa.Empresa-borrar'),
   url(r'^detalleEmpresa/(?P<pk>[\w\-]+)/$', EmpresaDetailView.as_view(), name='Empresa.Empresa-detalle'),
   # url(r'^detalleEmpresaPublic/(?P<pk>[\w\-]+)/$', EmpresaPublicDetailView.as_view(), name='Empresa.Empresa-detalle-public'),


 
]