from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from certificado.models import Certificado
from usuario.models import Usuario
from empresaCliente.models import EmpresaCliente
from .forms import CertificadoForm

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render_to_response
from django.db.models import Q

# Create your views here.
class CertificadoListView(ListView):
	model = Certificado
	template_name = 'certificado/certificado-list.html'
	#ordering = 'nombre'
	paginate_by = 10

	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)
		if self.request.GET.get('numero'):
			queryset = self.model.objects.filter(numero__contains=self.request.GET.get('numero'),
				expide=usuario.id_empresa)
		else:
			queryset = self.model.objects.filter(expide=usuario.id_empresa)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(CertificadoListView, self).get_context_data(**kwargs)
		if not context.get('is_paginated', False):
			return context

		paginator = context.get('paginator')
		num_pages = paginator.num_pages
		current_page = context.get('page_obj')
		page_no = current_page.number

		if num_pages <= 17 or page_no <= 9:  # case 1 and 2
		    pages = [x for x in range(1, min(num_pages + 1, 18))]
		elif page_no > num_pages - 9:  # case 4
			pages = [x for x in range(num_pages - 16, num_pages + 1)]
		else:  # case 3
			pages = [x for x in range(page_no - 7, page_no + 8)]

		context.update({'pages': pages})
		return context

class CertificadoCreateView(CreateView):
	model = Certificado
	template_name='certificado/certificado-form.html'
	form_class = CertificadoForm

	def get_context_data(self,**kwargs):
		context = super(CertificadoCreateView, self).get_context_data(**kwargs)
		context['titulo']='Ingresar Certificado'
		context['nombre_btn']='Guardar'
		return context

	def get_success_url(self):
		messages.success(self.request, 'El certificado ha sido creado con exito!.')
		return reverse('certificado.certificado-list')

	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('certificado.add_certificado'):
			return redirect(settings.LOGIN_URL)
		return super(CertificadoCreateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self,form):
		form.instance.owner = self.request.user
		return super(CertificadoCreateView,self).form_valid(form)

class CertificadoUpdateView(UpdateView):
	model = Certificado
	template_name='certificado/certificado-form.html'
	form_class = CertificadoForm

	def get_context_data(self,**kwargs):
		context = super(CertificadoUpdateView, self).get_context_data(**kwargs)
		context['titulo']='Actualizar Certificado'
		context['nombre_btn']='Actualizar'
		return context

	def get_success_url(self):
		messages.success(self.request, 'El certificado ha sido actualizado con exito!.')
		return reverse('certificado.certificado-list')

	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('certificado.change_certificado'):
			return redirect(settings.LOGIN_URL)
		return super(CertificadoUpdateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self,form):
		form.instance.owner = self.request.user
		return super(CertificadoUpdateView,self).form_valid(form)

class CertificadoDeleteView(DeleteView):
	template_name='certificado/confirmar-eliminacion.html'
	model = Certificado

	def get_success_url(self):
		messages.success(self.request, 'El certificado ha sido eliminado con exito!.')
		return reverse_lazy('certificado.certificado-list')

	def dispatch(self,request,*args,**kwargs):
		if not request.user.has_perms('certificado.delete_certificado'):
			return redirect(settings.LOGIN_URL)
		return super(CertificadoDeleteView,self).dispatch(request, *args, **kwargs)

class CertificadoDetailView(DetailView):
	model = Certificado
	template_name='certificado/certificado-detalle.html'

class CertificadoPublicDetailView(DetailView):
	model = Certificado
	template_name='certificado/certificado-detalle-public.html'

def search_view(request):
	query = request.GET.get('q', '')
	codigoSeguridad = request.GET.get('codigoSeguridad', '')
	if query and codigoSeguridad:
		qset = (
			Q(numero=query)&
			Q(codigoSeguridad=codigoSeguridad)
			)
		results = Certificado.objects.filter(qset).distinct()
	else:
		results=[]
	return render_to_response('certificado/search.html',{
		"results": results,
		"query": query
		})

