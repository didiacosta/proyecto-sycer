from django import forms

from .models import Empresa

class EmpresaForm(forms.ModelForm):
	logo = forms.ImageField()
	class Meta:
		model=Empresa
		fields=('nit','nombre','logo','resolucion','direccion','telefono')
		labels = {
			'body':'Texto'
		}
		# widgets = {
		# 	'nit': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'nombre': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'logo': forms.....,
		# 	'resolucion': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'direccion': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'telefono': forms.TextInput(attrs={'class': 'form-control'}),

		# }