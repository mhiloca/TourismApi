from rest_framework import viewsets

from core.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(viewsets.ModelViewSet):

    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filterset_fields =['name', 'description']

