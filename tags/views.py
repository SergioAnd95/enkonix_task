from rest_framework import viewsets

from .serializers import TagSerializer
from .models import Tag


class TagViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing tag instances.
    """
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
