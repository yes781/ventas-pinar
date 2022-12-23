from django.db import models


class Iteraciones(models.Model):
    n = models.FloatField()
    xn = models.FloatField()
    yn = models.FloatField()

    def __str__(self):
        return 'Iteraciones'
