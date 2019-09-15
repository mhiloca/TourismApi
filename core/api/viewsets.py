from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from core.models import PontoTuristico
from teste.api.viewsets import TesteViewSet
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    # http_method_names = ['get']

    def get_queryset(self):
        return PontoTuristico.objects.all().filter(status=True)

    @action(methods=['post', 'get'], detail=False)
    def teste(self, request, pk=None):
        return Response(TesteViewSet.queryset)


