from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Dictamen
from usuario.models import Usuario

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings

from .forms import DictamenForm

from evaluacionDictamen.models import EvaluacionDictamen

# Create your views here.
class DictamenListView(ListView):
	model=Dictamen
	template_name = 'dictamen/dictamen-list.html'
	paginate_by = 20


	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)
		queryset= self.model.objects.filter(organismo=usuario.id_empresa).order_by('municipio__departamento__nombre',
			'municipio__nombre')

		return queryset

class DictamenCreateView(CreateView):
	model = Dictamen
	template_name='dictamen/dictamen-form.html'
	form_class = DictamenForm		
	
	def get_success_url(self):
		messages.success(self.request, 'El Dictamen ha sido creado con exito! es necesario completar el registro con la evaluacion.')
		return reverse('dictamen.dictamen-list')

	def get_context_data(self,**kwargs):
		context = super(DictamenCreateView, self).get_context_data(**kwargs)
		context['titulo']='Ingresar Dictamen'
		context['nombre_btn']='Guardar'
		return context

	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('dictamen.add_dictamen'):
			return redirect(settings.LOGIN_URL)
		return super(DictamenCreateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self,form):
		form.instance.owner = self.request.user
		return super(DictamenCreateView,self).form_valid(form)

	def get_form_kwargs(self, **kwargs):
		kwargs = super(DictamenCreateView, self).get_form_kwargs(**kwargs)
		kwargs['initial']['owner'] = self.request.user.id
		return kwargs

class DictamenUpdateView(UpdateView):
	model = Dictamen
	template_name='dictamen/dictamen-form.html'
	form_class = DictamenForm

	def get_success_url(self):
		messages.success(self.request, 'El Dictamen ha sido actualizado con exito!')
		return reverse('dictamen.dictamen-list')

	def get_context_data(self,**kwargs):
		context = super(DictamenUpdateView, self).get_context_data(**kwargs)
		context['titulo']='Modificar Dictamen'
		context['nombre_btn']='Actualizar'
		return context

	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('dictamen.change_dictamen'):
			return redirect(settings.LOGIN_URL)
		return super(DictamenUpdateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self,form):
		form.instance.owner = self.request.user
		return super(DictamenUpdateView,self).form_valid(form)

	def get_form_kwargs(self, **kwargs):
		kwargs = super(DictamenUpdateView, self).get_form_kwargs(**kwargs)
		kwargs['initial']['owner'] = self.request.user.id
		return kwargs

class DictamenDetailView(ListView):
	model=EvaluacionDictamen
	template_name='dictamen/dictamen-detalle.html'
	paginate_by=20

	def get_queryset(self):
		print self.kwargs
		dictamen=Dictamen.objects.get(id=self.kwargs['idDictamen'])
		queryset = self.model.objects.filter(dictamen=dictamen)
		return queryset

	def get_context_data(self,**kwargs):
		context = super(DictamenDetailView, self).get_context_data(**kwargs)
		dictamen=Dictamen.objects.get(id=self.kwargs['idDictamen'])
		context['dictamenNumero']= dictamen.numero
		context['dictamenId']=dictamen.id
		context['tipo']=dictamen.nombreTipo
		context['cliente']=dictamen.cliente.id_cliente.nombre
		context['estado']=dictamen.aprobada
		context['ubicacion']=dictamen.municipio
		context['director']=dictamen.director_tecnico
		context['inspector']=dictamen.inspector
		context['responsableDiseno']=dictamen.responsableDiseno
		context['matResponsableDiseno']=dictamen.matriculaResponsableDiseno
		context['resInterventoria']=dictamen.responsableInterventoria
		context['matResInterventoria']=dictamen.matriculaInterventoria
		context['constructor'] = dictamen.responsableContruccion
		context['matConstructor'] = dictamen.matriculaResponsableContruccion
		return context


