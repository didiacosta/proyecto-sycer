from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import EvaluacionDictamen
# Create your views here.
def guardarEvaluacion(request):
	dictamen=None
	for x in request.GET:
		print x
		print 'valor' + request.GET[x]
		e=None
		e = EvaluacionDictamen.objects.get(id=x)
		e.respuesta=request.GET[x]
		dictamen=e.dictamen
		e.save()
	mensaje='La evaluacion se ha actualizado correctamente'
	#return render(request, '../dictamen/detalleDictamen/'+str(dictamen.id)+'/', {'mensaje': mensaje})
	messages.success(request, mensaje)
	return HttpResponseRedirect(reverse('Dictamen.Dictamen-detalle',
		kwargs={'idDictamen':dictamen.id}),{'mensaje':mensaje})
