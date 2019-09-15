from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from reviews.models import Review
from locations.models import Location


class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField(default=True)
    attraction_list = models.ManyToManyField(Attraction)
    comment_list = models.ManyToManyField(Comment)
    review_list = models.ManyToManyField(Review)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        db_constraint=False,
        default=0,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

