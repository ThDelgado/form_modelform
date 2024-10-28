from django.shortcuts import render, redirect
from .models import Libros
from django.http import HttpResponse
from .forms import LibroForm
from django.forms import ValidationError
from django.contrib import messages

# Create your views here.

def newbook(request):
    return render(request,"books/newbook.html", {})

def listbook(request):
    libros = Libros.objects.all()
    contexto = {}  
    contexto["libros"] = libros
    
    return render(request,"books/listbook.html", contexto)


                   
def add_libro_modelform(request):

    if request.method == 'GET':
        form = LibroForm()
        contexto = {'form': form}
        return render(request, "books/add_libro_modelform.html", contexto)
    
    

        #logica para procesar los datos.
    if request.method == 'POST':
        form = LibroForm(request.POST)
        

        if form.is_valid():
            try:  
                libro = form.save(commit=False)
                libro.clean()         
                libro.save()
                messages.success(request, "Libro creado correctamente")
                return redirect('listbook')
            except ValidationError as e:
                messages.error(request, e.messages )

        else:
            
            messages.error(request, "Error al intentar crear el producto, intente nuevamente")
            return render(request, "books/add_libro_modelform.html", {"form": LibroForm()})
            
      
    contexto = {"form": form}
    return render(request, "books/add_libro_modelform.html", contexto)