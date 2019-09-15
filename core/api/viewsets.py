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

    # def list(self, request, *args, **kwargs):
    #     pass
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass
    #
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # @action(methods=['post'], detail=True)
    # def denunciate(self, request, pk=None):
    #     pass

    @action(methods=['post', 'get'], detail=False)
    def teste(self, request, pk=None):
        return Response(TesteViewSet.queryset)


