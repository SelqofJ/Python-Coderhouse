from django.shortcuts import render
from django.http import HttpResponse
from estudiantes.models import Estudiante

from datetime import datetime

def saludar(request):
    return HttpResponse(f'Hola baby!!. Hora: {datetime.now()}')

def listar_estudiantes(request):
    contexto {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request = request, template_name='estudiantes/lista_estudiantes.html', 
        context = contexto
    )

"""def saludar2(request):
    return HttpResponse('Hola chickenfingers!!')

def saludar2(request):
    return HttpResponse('Hola chickenfingers!!')
# Create your views here.

"""