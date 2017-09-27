from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from empresaCliente.models import EmpresaCliente
from usuario.models import Usuario
from cliente.models import Cliente
from empresaCliente.forms import EmpresaClienteForm

from django.shortcuts import redirect
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings

# Create your views here.

class EmpresaClienteListView(ListView):
	model = EmpresaCliente
	template_name = 'empresaCliente/empresaCliente-list.html'
	#ordering = 'nombre'
	paginate_by = 10

	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)
		queryset= self.model.objects.filter(id_empresa=usuario.id_empresa)	
		return queryset

class EmpresaClienteDetailView(DetailView):
	model = Cliente
	template_name='empresaCliente/editarEmpresaCliente.html'


class EmpresaClienteUpdateView(UpdateView):
	model = Cliente
	template_name='empresaCliente/empresaCliente-form.html'
	form_class = EmpresaClienteForm
	#success_url = '/empresaCliente/clientes'


	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('cliente.change_cliente'):
			return redirect(settings.LOGIN_URL)
		return super(EmpresaClienteUpdateView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self,**kwargs):
		context = super(EmpresaClienteUpdateView, self).get_context_data(**kwargs)
		context['titulo']='Editar Cliente'
		context['nombre_btn']='Actualizar'
		return context

	def get_success_url(self):
		messages.success(self.request, 'El cliente ha sido actualizado con exito!.')
		return reverse('empresaCliente.empresaCLiente-list')

class EmpresaClienteCreateView(CreateView):
	model = Cliente
	template_name='empresaCliente/empresaCliente-form.html'
	form_class = EmpresaClienteForm		
	
	def get_success_url(self):
		usuario = Usuario.objects.get(user=self.request.user)
		empresaCli = EmpresaCliente(id_empresa=usuario.id_empresa,id_cliente=self.model.objects.order_by('-id')[0])
		empresaCli.save()
		messages.success(self.request, 'El cliente ha sido creado con exito!.')
		return reverse('empresaCliente.empresaCLiente-list')

	def get_context_data(self,**kwargs):
		context = super(EmpresaClienteCreateView, self).get_context_data(**kwargs)
		context['titulo']='Ingresar Cliente'
		context['nombre_btn']='Guardar'
		return context

	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('cliente.add_cliente'):
			return redirect(settings.LOGIN_URL)
		return super(EmpresaClienteCreateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self,form):
		form.instance.owner = self.request.user
		return super(EmpresaClienteCreateView,self).form_valid(form)

class EmpresaClienteDeleteView(DeleteView):
	template_name='empresaCliente/confirmar-eliminacion.html'
	model = EmpresaCliente

	def get_success_url(self):
		messages.success(self.request, 'El cliente ha sido eliminado con exito!.')
		return reverse_lazy('empresaCliente.empresaCLiente-list')

	def dispatch(self,request,*args,**kwargs):
		if not request.user.has_perms('empresaCliente.delete_empresaCliente'):
			return redirect(settings.LOGIN_URL)
		return super(EmpresaClienteDeleteView,self).dispatch(request, *args, **kwargs)


from io import BytesIO

from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

def generar_pdf(request):
	print "Genero el PDF"
	response = HttpResponse(content_type='application/pdf')
	pdf_name = "clientes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
	buff = BytesIO()
	doc = SimpleDocTemplate(buff,
							pagesize=letter,
							rightMargin=40,
							leftMargin=40,
							topMargin=60,
							bottomMargin=18,
							)
	clientes = []
	styles = getSampleStyleSheet()
	header = Paragraph("Listado de Clientes", styles['Heading1'])
	clientes.append(header)
	headings = ('Nit', 'Nombre')
	usuario= Usuario.objects.get(user=request.user)
	
	allclientes = [(p.id_cliente.nit, p.id_cliente.nombre) for p in EmpresaCliente.objects.filter(id_empresa=usuario.id_empresa)]
	print allclientes

	t = Table([headings] + allclientes)
	t.setStyle(TableStyle(
		[
			('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
			('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
			('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
		]
	))
	clientes.append(t)
	doc.build(clientes)
	response.write(buff.getvalue())
	buff.close()
	return response