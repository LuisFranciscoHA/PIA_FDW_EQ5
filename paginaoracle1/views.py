from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'paginaoracle1/index.html')

def caracteristicas(request):
    return render(request, 'paginaoracle1/caracteristicas.html')
