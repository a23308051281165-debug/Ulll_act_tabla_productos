from django.db import models

# ==========================================
# MODELO: PRODUCTO
# ==========================================
class Producto(models.Model):
    ID_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    UNIDADES = [
        ('kg', 'Kilogramo'),
        ('gr', 'Gramo'),
        ('L', 'Litro'),
        ('unidad', 'Unidad'),
    ]
    unidad_medida = models.CharField(max_length=10, choices=UNIDADES, default='unidad')

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"
