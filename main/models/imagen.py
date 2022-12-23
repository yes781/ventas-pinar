from django.db import models
from main.models import Producto


class Imagen(models.Model):
    iamgen = models.ImageField(upload_to='imagenes')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.iamgen.url)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
