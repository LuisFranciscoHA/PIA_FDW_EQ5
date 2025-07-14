from django.shortcuts import render
from .models import tecnologia_apoyo


# Create your views here.
def inicio(request):
    return render(request, 'paginaoracle1/index.html')

def caracteristicas(request):
    return render(request, 'paginaoracle1/caracteristicas.html')

def ventajas_view(request):
    return render(request, 'paginaoracle1/ventajas.html')

def desventajas(request):
    return render(request, 'paginaoracle1/desventajas.html')

def apoyo(request):
    tecnologias = tecnologia_apoyo.objects.all()
    return render(request, 'paginaoracle1/apoyo.html', {'tecnologias': tecnologias})

def contacto(request):
    return render(request, 'paginaoracle1/contacto.html')

def java(request):
    return render(request, 'paginaoracle1/javascript_leng.html')
