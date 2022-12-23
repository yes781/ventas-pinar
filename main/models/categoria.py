from django.db import models


class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=100, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de Creacion', max_length=150, blank=False, null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
