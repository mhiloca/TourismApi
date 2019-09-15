from rest_framework import viewsets
from .serializers import TesteSerializer
from teste.models import Teste


class TesteViewSet(viewsets.ModelViewSet):

    queryset = Teste.objects.all()
    serializer_class = TesteSerializer
