from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from Familia.models import Familia
# Create your views here.

def familiares(request):
    
    familiar1 = Familia(nombre = "Susana", edad = 59, nacimiento = "1963-08-22" )
    #familiar1.save()
    familiar2 = Familia(nombre = "Mariel", edad = 27, nacimiento = "1995-07-26" )
    #familiar2.save()
    familiar3 = Familia(nombre = "Engracia", edad = 84, nacimiento = "1938-07-09")
    #familiar3.save()

    diccionario = {"familiar1":familiar1, "familiar2":familiar2, "familiar3":familiar3}

    return render(request, "Familia/familia.html", context = diccionario)

