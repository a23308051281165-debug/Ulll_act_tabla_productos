from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('ID_producto', 'nombre', 'categoria', 'precio', 'stock', 'unidad_medida')
    search_fields = ('nombre', 'categoria')
