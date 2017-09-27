from django import forms

from .models import Certificado

class CertificadoForm(forms.ModelForm):
	class Meta:
		model = Certificado
		fields =('id_empresa_cliente','nombre','descripcion','ruta','observacion',
			'tipo','pesoArchivo','fecha','numero','codigoSeguridad','municipio')
		labels = {
			'body':'Texto'
		}
		widgets = {
		# 	'id_empresa_cliente': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'nombre': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'ruta': forms.FileField(),
		# 	'observacion': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'tipo': forms.TextInput(attrs={'class': 'form-control'}),
		'fecha': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'AAAA-MM-DD'}),
		# 	'numero': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'municipio': forms.TextInput(attrs={'class': 'form-control'}),
		}

