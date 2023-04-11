from django.db import models

# Create your models here.

class productos(models.Model):
    nombre_producto = models.CharField(max_length=25)
    precio_producto = models.IntegerField()
    vencimiento_producto = models.DateField()
    descripcion_producto = models.CharField(max_length=60)

    def __str__(self):
        return f"Producto: {self.nombre_producto} - Precio: ${self.precio_producto} - Vencimiento: {self.vencimiento_producto} - Descripción: {self.descripcion_producto}"