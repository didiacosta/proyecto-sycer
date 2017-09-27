from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

from certificado import views

#from usuario import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sycer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuario/', include('usuario.urls')),
    url(r'^empresaCliente/', include('empresaCliente.urls')),
    url(r'^certificado/', include('certificado.urls')),
    url(r'^sycer/$', views.search_view, name='sycer.busqueda'),
    url(r'^empresa/', include('empresa.urls')),
    url(r'^empresaInspector/', include('empresaInspector.urls')),
    url(r'^dictamen/', include('dictamen.urls')),
    #url(r'^$', 'usuario.views.index_view', name='usuario.index'),
    #url(r'^login/$', 'usuario.views.login_view', name='usuario.login'),
)

urlpatterns += patterns('',url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),)
