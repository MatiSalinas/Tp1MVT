from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template, Context
from familia.models import *

# Create your views here.

def lista_familiares(request):
    familiares = Familiares.objects.all()

    familiares_lista = []
    
    for familiar in familiares:
        familiares_lista.append(familiar)
    
    datos = {'familiares':familiares_lista}
    plantilla = loader.get_template('familiares.html')
    documento = plantilla.render(datos)

    return HttpResponse(documento)


