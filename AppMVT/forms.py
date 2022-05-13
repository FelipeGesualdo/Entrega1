from django import forms

class EntrenamientoForm(forms.Form):
    deporte = forms.CharField(max_length=50)
    precio_por_hora = forms.IntegerField()

class JugadoresForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()

class MaterialesForm(forms.Form):
    material = forms.CharField(max_length=50)
    costo = forms.IntegerField()