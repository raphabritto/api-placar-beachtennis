from rest_framework import viewsets

from .serializers import TorneiosSerializer
from .models import Torneios


class TorneiosViewSet(viewsets.ModelViewSet):
    serializer_class = TorneiosSerializer
    queryset = Torneios.objects.all()
    