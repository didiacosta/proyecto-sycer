from django import forms

from .models import Cliente

class EmpresaClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields =('nit','nombre', 'estado')
		labels = {
			'body':'Texto'
		}
		widgets = {
			'nit': forms.TextInput(attrs={'class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'estado': forms.NumberInput(attrs={'class': 'form-control','min':'0','max':'1','step':'1'}),
		}