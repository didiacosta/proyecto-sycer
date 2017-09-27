from django import forms

from .models import Inspector

class EmpresaInspectorForm(forms.ModelForm):
	class Meta:
		model = Inspector
		fields =('nombres','apellidos', 'matricula_profesional', 'activo')
		labels = {
			'body':'Texto'
		}
		widgets = {
			'nombres': forms.TextInput(attrs={'class': 'form-control'}),
			'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
			'matricula_profesional': forms.TextInput(attrs={'class': 'form-control'}),
		}