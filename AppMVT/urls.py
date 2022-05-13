from django.urls import path
from .views import *

urlpatterns = [
    path('entrenamiento/',entrenamiento, name='entrenamiento'),
    path('jugadores/', jugadores, name='jugadores'),
    path('materiales/', materiales, name='materiales'),
    path('',inicio, name='inicio'),
    path('buscar/', buscar, name="buscar" ),
    
]