from django.shortcuts import render
from blog.views import categoria

from tienda.models import CategoriaProducto, Producto

# Create your views here.

def tienda(request):
    productos=Producto.objects.all()
    categorias=CategoriaProducto.objects.all()
    return render(request, 'tienda/tienda.html',{'productos':productos, 'categorias':categorias})

