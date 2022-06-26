from django.http import HttpResponse
from django.template import loader, Template, Context
from django.shortcuts import render

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
    render1 = template1.render({"nombre":nombre,"apellido":apellido,"lista": lista})
    return HttpResponse(render1)

