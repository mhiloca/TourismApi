from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from reviews.models import Review
from locations.models import Location
from teste.models import Teste


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
        default=0
    )
    mock_test = models.ManyToManyField(Teste)
    photo = models.ImageField(upload_to='touristic_places', null=True, blank=True)

    def __str__(self):
        return self.name

