from django.shortcuts import render
from blog.models import Post, Categoria
# Create your views here.

def blog(request):
    posts=Post.objects.all() 
    categorias=Categoria.objects.all() 
    return render(request, 'blog/blog.html',{'posts':posts, 'categorias':categorias})

def categoria(request, categoria_id):
    todas_categorias=Categoria.objects.all()
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, 'blog/categoriasblog.html', {'categoria':categoria,'posts':posts, 'todas_categorias':todas_categorias})