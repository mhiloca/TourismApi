from rest_framework import serializers

from core.models import PontoTuristico

from attractions.api.serializers import AttractionSerializer
from comments.api.serializers import CommentSerializer
from reviews.api.serializers import ReviewSerializer
from locations.api.serializers import LocationSerializer



class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:

        model = PontoTuristico
        fields = ('id',
                  'name',
                  'description',
                  'status',
                  'photo'
                  )

class CompletePontoTuristicoSerializer(serializers.ModelSerializer):
    attraction_list = AttractionSerializer(many=True)
    location = LocationSerializer()
    review_list = ReviewSerializer(many=True)
    comment_list = CommentSerializer(many=True)

    class Meta:

        model = PontoTuristico
        fields = [
            'id',
            'name',
            'description',
            'status',
            'location',
            'attraction_list',
            'comment_list',
            'review_list'
        ]
