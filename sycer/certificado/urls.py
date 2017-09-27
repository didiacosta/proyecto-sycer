from django.conf.urls import patterns,url

from certificado.views import CertificadoListView, CertificadoCreateView, CertificadoUpdateView, CertificadoDeleteView, CertificadoDetailView, CertificadoPublicDetailView
from . import views

urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
   #url(r'^$', views.BusquedaCertificadoInicio_view, name='certificado.index'),
    url(r'^certificados/$', CertificadoListView.as_view(), name='certificado.certificado-list'),
    url(r'^crearCertificado/$', CertificadoCreateView.as_view(), name='certificado.certificado-crear'),
    url(r'^editarCertificado/(?P<pk>[\w\-]+)/$', CertificadoUpdateView.as_view(), name='certificado.certificado-editar'),
    url(r'^borrarCertificado/(?P<pk>[\w\-]+)/$', CertificadoDeleteView.as_view(), name='certificado.certificado-borrar'),
    url(r'^detalleCertificado/(?P<pk>[\w\-]+)/$', CertificadoDetailView.as_view(), name='certificado.certificado-detalle'),
    url(r'^detalleCertificadoPublic/(?P<pk>[\w\-]+)/$', CertificadoPublicDetailView.as_view(), name='certificado.certificado-detalle-public'),


 
]