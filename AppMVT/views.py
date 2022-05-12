from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def entrenamiento(request):
    entrenamiento = Entrenamiento(deporte="Futbol", precio_por_hora=400)
    entrenamiento.save()
    return HttpResponse(f"Entrenamiento creado:{entrenamiento.deporte},{entrenamiento.precio_por_hora}")

def jugadores(request):
    jugadores = Jugadores(nombre="Felipe", edad=19)
    jugadores.save()
    return HttpResponse(f"Jugador creado:{jugadores.nombre},{jugadores.edad}")

def materiales(request):
    materiales = Materiales(material="Pelota", costo=2000)
    materiales.save()
    return HttpResponse(f"Material creado:{materiales.material},{materiales.costo}")


