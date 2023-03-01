from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import  Libros
from .formulario import Libroform

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nossotros (request):
  return render(request, 'paginas/nosotros.html')

# CRUD con funciones
def libros(request):
    libros= Libros.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crearLibro(request):
    formulario = Libroform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editarLibro(request, id):
    libro = Libros.objects.get(id=id)
    formulario = Libroform(request.POST or None, request.FILES or  None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminarLIbro(request, id):
    libro = Libros.objects.get(id = id)
    libro.delete()
    return redirect( 'libros')

