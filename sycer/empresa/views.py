from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Empresa
from usuario.models import Usuario

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render_to_response
from django.db.models import Q
# Create your views here.

from empresa.forms import EmpresaForm

class EmpresaDetailView(DetailView):
	model = Empresa
	template_name='empresa/empresa-detalle.html'

class EmpresaUpdateView(UpdateView):
	model = Empresa
	template_name='empresa/empresa-form.html'
	form_class = EmpresaForm
	
	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('empresa.change_empresa'):
			return redirect(settings.LOGIN_URL)
		return super(EmpresaUpdateView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self,**kwargs):
		context = super(EmpresaUpdateView, self).get_context_data(**kwargs)
		context['titulo']='Editar Organismo'
		context['nombre_btn']='Actualizar'
		return context

	def get_success_url(self):
		emp=self.request.user.usuario.id_empresa.id
		messages.success(self.request, 'El organismo ha sido actualizado con exito!.')
		return reverse('Empresa.Empresa-detalle', args=(emp,))
