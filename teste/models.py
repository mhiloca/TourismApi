from django.db import models


class Teste(models.Model):
    anything = models.CharField(max_length=100)

    def __str__(self):
        return self.anything
