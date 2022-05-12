from django.db import models

class Entrenamiento(models.Model):
    deporte = models.CharField(max_length=50)
    precio_por_hora = models.IntegerField()

    def __str__(self):
        return self.deporte+"---->precio por hora:"+self.precio_por_hora



class Jugadores(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()

class Materiales(models.Model):
    material = models.CharField(max_length=50)
    costo = models.IntegerField()
