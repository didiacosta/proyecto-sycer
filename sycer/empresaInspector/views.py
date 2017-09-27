from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import EmpresaInspector
from usuario.models import Usuario
from inspector.models import Inspector

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from .forms import EmpresaInspectorForm

# Create your views here.

class EmpresaInspectorListView(ListView):
	model = EmpresaInspector
	template_name = 'empresaInspector/empresaInspector-list.html'
	#ordering = 'nombres'
	paginate_by = 20

	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)
		queryset= self.model.objects.filter(empresa=usuario.id_empresa).order_by('inspector__nombres',
		 'inspector__apellidos')	
		return queryset

class EmpresaInspectorCreateView(CreateView):
	model = Inspector
	template_name='empresaInspector/empresaInspector-form.html'
	form_class = EmpresaInspectorForm		
	
	def get_success_url(self):
		usuario = Usuario.objects.get(user=self.request.user)
		empresaIns = EmpresaInspector(empresa=usuario.id_empresa,
			inspector=self.model.objects.order_by('-id')[0])
		empresaIns.save()
		messages.success(self.request, 'El inspector ha sido creado con exito!.')
		return reverse('empresaInspector.empresaInspector-list')

	def get_context_data(self,**kwargs):
		context = super(EmpresaInspectorCreateView, self).get_context_data(**kwargs)
		context['titulo']='Ingresar inspector'
		context['nombre_btn']='Guardar'
		return context

	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('inspector.add_inspector'):
			return redirect(settings.LOGIN_URL)
		return super(EmpresaInspectorCreateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self,form):
		form.instance.owner = self.request.user
		return super(EmpresaInspectorCreateView,self).form_valid(form)

class EmpresaInspectorUpdateView(UpdateView):
	model = Inspector
	template_name='empresaInspector/empresaInspector-form.html'
	form_class = EmpresaInspectorForm
	#success_url = '/empresaCliente/clientes'


	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('inspector.change_inspector'):
			return redirect(settings.LOGIN_URL)
		return super(EmpresaInspectorUpdateView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self,**kwargs):
		context = super(EmpresaInspectorUpdateView, self).get_context_data(**kwargs)
		context['titulo']='Editar Inspector'
		context['nombre_btn']='Actualizar'
		return context

	def get_success_url(self):
		messages.success(self.request, 'El inspector ha sido actualizado con exito!.')
		return reverse('empresaInspector.empresaInspector-list')

class EmpresaInspectorDeleteView(DeleteView):
	template_name='empresaInspector/confirmar-eliminacion.html'
	model = EmpresaInspector

	def get_success_url(self):
		messages.success(self.request, 'El inspector ha sido eliminado con exito!.')
		return reverse_lazy('empresaInspector.empresaInspector-list')

	def dispatch(self,request,*args,**kwargs):
		if not request.user.has_perms('empresaInspector.delete_empresaInspector'):
			return redirect(settings.LOGIN_URL)
		return super(EmpresaInspectorDeleteView,self).dispatch(request, *args, **kwargs)