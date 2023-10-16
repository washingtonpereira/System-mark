from django.shortcuts import render
from core.models import Consulta


# Create your views here.

def lista_consultas(request):
    consulta = Consulta.objects.get(id=1)
    response = {'consulta':consulta}
    return render(request, 'agenda.html', response) 