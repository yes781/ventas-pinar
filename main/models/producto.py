from django.contrib.auth.models import User
from django.db import models
from .categoria import Categoria


class Producto(models.Model):
    nombre = models.CharField('Nombre del Producto', max_length=100, blank=False, null=False)
    precio = models.FloatField('Presio', max_length=7, blank=False, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
