from django import forms

from .models import Dictamen
from inspector.models import Inspector
from empresaCliente.models import EmpresaCliente
from django.contrib.auth.models import User
from usuario.models import Usuario
from empresa.models import Empresa
from empresaInspector.models import EmpresaInspector
from inspector.models import Inspector

class DictamenForm(forms.ModelForm):
	userId=None
	def __init__(self, *args, **kwargs):
		self.userId = kwargs['initial']['owner']
		print self.userId
		super(DictamenForm, self).__init__(*args, **kwargs)
		usuario= Usuario.objects.get(user=self.userId)
		#consulto los clientes de la empresa del usuario actual
		choices=[(pt.id_cliente.id,pt.id_cliente.nombre) for pt in EmpresaCliente.objects.filter(id_empresa=usuario.id_empresa)]
		self.fields['cliente'].choices = choices
		#consulto la empresa actual
		empresa = Empresa.objects.filter(id=usuario.id_empresa.id)
		self.fields['organismo'].choices = [
			(e.id,unicode(e)) for e in Empresa.objects.filter(id=usuario.id_empresa.id)
		]
		#consulto los inspectores de la empresa actual
		self.fields['inspector'].choices = [
			(i.inspector.id, unicode(i.inspector)) for i in EmpresaInspector.objects.filter(empresa=usuario.id_empresa)
		]

		#consulto los directores tecnicos
		self.fields['director_tecnico'].choices = [
			(i.inspector.id, unicode(i.inspector)) for i in EmpresaInspector.objects.filter(empresa=usuario.id_empresa)
		]

	inspector = forms.ModelChoiceField(queryset=Inspector.objects.all())
	
	

	class Meta:
		model = Dictamen
		fields =('organismo','cliente','tipo', 'numero','director_tecnico','inspector','numero','municipio',
			'responsableDiseno','matriculaResponsableDiseno','responsableInterventoria',
			'matriculaInterventoria','responsableContruccion','matriculaResponsableContruccion',
			'anexos','observaciones',)
		labels = {
		 	'body':'Texto'
		}
		#widgets = {
		#	'cliente': forms.SelectInput(attrs={'class': 'form-control'}),
		# 	'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'matricula_profesional': forms.TextInput(attrs={'class': 'form-control'}),
		#}

