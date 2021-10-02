from rest_framework import viewsets
from .serializers import TrackSerializer
from .models import Track

class TracksViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer