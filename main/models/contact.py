from django.db import models
from django.contrib.auth.models import User


class MyContact(models.Model):
    name = models.CharField('Contacto', max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    have_contact = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.name
