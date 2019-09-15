from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import PontoTuristico
from teste.api.viewsets import TesteViewSet
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    # http_method_names = ['get']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset = PontoTuristico.objects.all()
        res = queryset
        if id:
            res = queryset.filter(id=id)

        if name:
            res = queryset.filter(name__iexact=name)

        if description:
            res = queryset.filter(description__iexact=description)

        return res.filter(status=True)



    # @action(methods=['post', 'get'], detail=False)
    # def teste(self, request, pk=None):
    #     return Response


