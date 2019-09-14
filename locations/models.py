from django.db import models


class Location(models.Model):
    line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.line1
