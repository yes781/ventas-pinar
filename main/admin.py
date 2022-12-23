from django.contrib import admin
from .models import *


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'fecha_creacion')


class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'precio', 'usuario')


class ImagenAdmin(admin.ModelAdmin):
    search_fields = ['nombre']


class ContactoAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'email', 'phone', 'user')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(MyContact, ContactoAdmin)
