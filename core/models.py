from django.db import models
from attractions.models import Attraction
from comments.models import Comment


class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField(default=True)
    attraction_list = models.ManyToManyField(Attraction)
    comment_list = models.ManyToManyField(Comment)

    def __str__(self):
        return self.name

