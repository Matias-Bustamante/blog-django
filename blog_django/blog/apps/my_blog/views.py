from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def home(request): 
    posts=Post.objects.filter(estado=True)
    querysets=request.GET.get("buscar")
    if querysets: 
        posts=Post.objects.filter( 
                Q(titulo__icontains=querysets) | 
                Q(descripcion__icontains=querysets)
        )
    paginator=Paginator(posts,3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'index.html',{'posts':posts})

def generales(request): 
    post=Post.objects.filter(estado=True,categoria=Categoria.objects.get(nombre__iexact='Generales')) 
    querysets=request.GET.get('buscar')

    if querysets: 
        posts=Post.objects.filter( 
           Q(titulo__icontains=querysets) | 
           Q(descripcion__icontains=querysets), 
           estado=True, 
           categoria=Categoria.objects.get(nombre__iexact='Generales')
                                
        )
    paginator=Paginator(posts,3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'generales.html', {'posts':post})

def detallePost(request,slug): 
    post=get_object_or_404(Post,slug=slug)
    return render(request,'detalle_post.html',{'detalle_post':post})

def programacion(request): 
    posts=Post.objects.filter(estado=True,categoria=Categoria.objects.get(nombre__iexact='Programacion')) 
    querysets=request.GET.get('buscar')

    if querysets: 
        posts=Post.objects.filter( 
           Q(titulo__icontains=querysets) | 
           Q(descripcion__icontains=querysets), 
           estado=True, 
           categoria=Categoria.objects.get(nombre__iexact='Programacion')
                                
        )
    paginator=Paginator(posts,3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'programacion.html',{'posts':posts})

def tecnologia(request): 
    posts=Post.objects.filter(estado=True,categoria=Categoria.objects.get(nombre__iexact='Tecnologia')) 
    querysets=request.GET.get('buscar')

    if querysets: 
        posts=Post.objects.filter( 
           Q(titulo__icontains=querysets) | 
           Q(descripcion__icontains=querysets), 
           estado=True, 
           categoria=Categoria.objects.get(nombre__iexact='Tecnologia')
                                
        )
    paginator=Paginator(posts,3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'tecnologia.html',{'posts':posts})

def tutoriales(request): 
    posts=Post.objects.filter(estado=True,categoria=Categoria.objects.get(nombre__iexact='Tutoriales')) 
    querysets=request.GET.get('buscar')

    if querysets: 
        posts=Post.objects.filter( 
           Q(titulo__icontains=querysets) | 
           Q(descripcion__icontains=querysets), 
           estado=True, 
           categoria=Categoria.objects.get(nombre__iexact='Tutoriales')
                                
        )
    paginator=Paginator(posts,3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'tutoriales.html',{'posts':posts})

def videojuegos(request): 
    posts=Post.objects.filter(estado=True,categoria=Categoria.objects.get(nombre__iexact='Videojuegos')) 
    querysets=request.GET.get('buscar')

    if querysets: 
        posts=Post.objects.filter( 
           Q(titulo__icontains=querysets) | 
           Q(descripcion__icontains=querysets), 
           estado=True, 
           categoria=Categoria.objects.get(nombre__iexact='Videojuegos')
                                
        )
    paginator=Paginator(posts,3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'videojuego.html',{'posts':posts})
    
