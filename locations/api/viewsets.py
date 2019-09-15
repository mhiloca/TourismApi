from rest_framework import viewsets
from locations.models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
