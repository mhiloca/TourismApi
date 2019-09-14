from django.db import models
from attractions.models import Attraction


class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField(default=True)
    attraction_list = models.ManyToManyField(Attraction)

    def __str__(self):
        return self.name

