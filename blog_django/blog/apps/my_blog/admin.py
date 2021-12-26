from django.contrib import admin
from .models import Categoria,Autor,Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource): 
    class Meta: 
        model=Categoria

class AutorResource(resources.ModelResource): 
    class Meta: 
        model=Autor 

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin): 
    search_fields=['nombre']
    list_display=('nombre','estado','fecha_creacion')
    resource_class=CategoriaResource

class AutorCategoria(ImportExportModelAdmin,admin.ModelAdmin): 
    search_fields=['nombres']
    list_display=('nombres','apellido','estado', 'fecha_creacion')
    resource_class=AutorResource 

# Register your models here.

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorCategoria)
admin.site.register(Post)

