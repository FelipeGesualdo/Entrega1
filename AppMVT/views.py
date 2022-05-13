from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppMVT.forms import *

def entrenamiento(request):
    if request.method == 'POST':
        formulario=EntrenamientoForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            entrenamiento=Entrenamiento(deporte = informacion['deporte'], precio_por_hora = informacion['precio_por_hora'])
            entrenamiento.save()
            return render(request,"AppMVT/inicio.html")
    else:
        formulario=EntrenamientoForm()
        return render(request,"AppMVT/entrenamiento.html",{'formulario':formulario})
    
    

def jugadores(request):
    if request.method == 'POST':
        formulario=JugadoresForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            jugadores=Jugadores(nombre = informacion['nombre'], edad = informacion['edad'])
            jugadores.save()
            return render(request,"AppMVT/inicio.html")
    else:
        formulario=JugadoresForm()
        return render(request,"AppMVT/jugadores.html",{'formulario':formulario})

    

def materiales(request):
    if request.method == 'POST':
        formulario=MaterialesForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            materiales=Materiales(material = informacion['material'], costo = informacion['costo'])
            materiales.save()
            return render(request,"AppMVT/inicio.html")
    else:
        formulario=MaterialesForm()
        return render(request,"AppMVT/materiales.html",{'formulario':formulario})
    
    

def inicio(request):
    return render (request,"AppMVT/inicio.html")

def buscar(request):
    if request.GET['nombre']:
        nombre= request.GET['nombre']
        jugador= Jugadores.objects.filter(nombre__icontains=nombre)
        return render(request,"AppMVT/resultados.html",{'jugadores':jugadores})
    else:
        respuesta= "No se ingresaron nombres"
        return render(request,"AppMVT/inicio.html",{'respuesta':respuesta})
        

    return render (request,"AppMVT/resultados.html")

#def entrenamientoFormulario(request):
    #return render (request,'AppMVT/entrenamientoFormulario.html')

#def jugadoresFormulario(request):
    #return render (request,'AppMVT/jugadoresFormulario.html')

#def materialesFormulario(request):
    #return render (request,'AppMVT/materialesFormulario.html')



#entrenamiento = Entrenamiento(deporte="Futbol", precio_por_hora=400)
    #entrenamiento.save()

#jugadores = Jugadores(nombre="Felipe", edad=19)
    #jugadores.save()

#materiales = Materiales(material="Pelota", costo=2000)
    #materiales.save()