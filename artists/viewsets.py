from rest_framework import viewsets
from .serializers import ArtistsSerializer
from .models import Artist

class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer