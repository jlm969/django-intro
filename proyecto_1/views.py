from django.http import HttpResponse
from datetime import datetime

#Siempre hay que pasarle a la funcion (request) en Django y una vista siempre retorna algo
def primer_vista(request):  
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):  
    return HttpResponse("<h1>Titulo 1</h1> <p>Esto es un parrafo </p>")

def dia_hora(request):
    fecha_hora = datetime.now
    return HttpResponse(f"<p>Tiempo Actual: {fecha_hora}</p>")


def nombre_usuario(request, nombre_usuario):
    nombre_usuario = datetime.now
    return HttpResponse(f"<p>Tu nomobre es : {nombre_usuario}</p>")    


def edad_usuario(request, edad):
    edad = datetime.now
    return HttpResponse(f"<p>Usted nacio en : {edad}</p>")   

