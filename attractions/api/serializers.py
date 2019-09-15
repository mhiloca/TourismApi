from rest_framework import serializers
from attractions.models import Attraction


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = (
            'name',
            'description',
            'work_hours',
            'min_age',
            'photo'
        )