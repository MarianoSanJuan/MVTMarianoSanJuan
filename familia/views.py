from django.http import HttpResponse
from django.template import loader, Template, Context
from django.shortcuts import render
from familia.models import Integrantesfamilia

# Create your views here.
# Creación de vista de familia


def home(request):
    
    template1 = loader.get_template("home.html")
    nombre = "Mariano"
    apellido = "San Juan"
    render1 = template1.render({"nombre":nombre,"apellido":apellido})
    return HttpResponse(render1)

def familia(request):
    
    template1 = loader.get_template("familia.html")
    nombre = "Mariano"
    apellido = "San Juan"
    lista = ["Andrés","Eugenia","Carolina","Ricardo"]
    listaedad = [33,24,62,64]
    
    render1 = template1.render({"nombre":nombre,"apellido":apellido,"lista": lista,"listaedad":listaedad})
    return HttpResponse(render1)


def familia_db(request):
    
    template1 = loader.get_template("familiadb.html")
    nombre = "Mariano"
    apellido = "San Juan"
    
    integrante = Integrantesfamilia(nombre = "Sofia", edad =29)
    # integrante.save()
    
    render1 = template1.render({"nombre":nombre,"apellido":apellido,"integrante":integrante})
    return HttpResponse(render1)

def familia_dburl(request,integrante_nombre, integrante_edad):
    
    template1 = loader.get_template("familiadburl.html")
    nombre = integrante_nombre
    edad = integrante_edad
    
    # integrante.save()
    
    render1 = template1.render({"nombre":nombre,"edad":edad})
    return HttpResponse(render1)