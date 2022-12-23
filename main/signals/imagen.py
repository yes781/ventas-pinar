from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

from main.models import Imagen


@receiver(post_delete, sender=Imagen)
def delete_imagen_posdelete(sender, instance: Imagen, **kwargs):
    try:
        os.remove(instance.iamgen.path)
    except:
        pass
