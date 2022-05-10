from django.db import models


# Create your models here.

class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=15)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name= 'categoriaproducto'
        verbose_name_plural = 'categoriaproductos'
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    articulo=models.CharField(max_length=50)
    categoria=models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE) 
    disponibilidad=models.BooleanField(default=True)
    descripcion=models.CharField(max_length=100)
    importe=models.FloatField()
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name= 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.articulo

    




