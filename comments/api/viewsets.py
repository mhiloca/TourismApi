from rest_framework import viewsets
from comments.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all().filter(status=True)
