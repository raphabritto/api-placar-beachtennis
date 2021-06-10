from rest_framework import viewsets

# from .serializers import TorneiosSerializer, NivelCategoriasSerializer, GeneroCategoriasSerializer
# from .models import Torneios, NivelCategorias, GeneroCategorias
from .serializers import *
from .models import *


class TorneiosViewSet(viewsets.ModelViewSet):
    serializer_class = TorneiosSerializer
    queryset = Torneios.objects.all()
    

class NivelCategoriasViewSet(viewsets.ModelViewSet):
    serializer_class = NivelCategoriasSerializer
    queryset = NivelCategorias.objects.all()


class GeneroCategoriasViewSet(viewsets.ModelViewSet):
    serializer_class = GeneroCategoriasSerializer
    queryset = GeneroCategorias.objects.all()


class TipoCategoriasViewSet(viewsets.ModelViewSet):
    serializer_class = TipoCategoriasSerializer
    queryset = TipoCategorias.objects.all()


class TorneioCategoriasViewSet(viewsets.ModelViewSet):
    serializer_class = TorneioCategoriasSerializer
    queryset = TorneioCategorias.objects.all()
        