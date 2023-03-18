from django.shortcuts import render

# Create your views here.

from .models import * 
 
# Create your views here. 
def verCategorias(request):     #Consultar categorias 
    listaCateg = Categoria.objects.all() 
 
    #ensamblar context     
    context = { 
        'categorias': listaCateg, 
        'titulo': 'Categorias de Productos del Supermercado',     } 
    #renderizar 
    return render(request, 'productos/categorias.html', context) 
