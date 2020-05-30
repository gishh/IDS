from django.shortcuts import render
from django.http import HttpResponse
from ARD.models import Personaje

def index(request):
    nombre = request.POST.get('nombre')
    nivel = request.POST.get('nivel')
    skill = request.POST.get('skill')
    if request.method == 'POST':
        personaje = Personaje()
        personaje.nombre = nombre
        personaje.nivel = nivel
        personaje.skill = skill
        personaje.save()

    #return HttpResponse("Bienvenidos a ADS")
    lista = Personaje.objects.all()
    return render(request,'ARD//index.html',{'lista':lista})
# Create your views here.
