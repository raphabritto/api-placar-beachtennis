from django.db.models import query
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
        

class EquipesViewSet(viewsets.ModelViewSet):
    serializer_class = EquipesSerializer
    queryset = Equipes.objects.all()


class JogosViewSet(viewsets.ModelViewSet):
    serializer_class = JogosSerializer
    queryset = Jogos.objects.all()


class PlacarViewSet(viewsets.ModelViewSet):
    serializer_class = PlacarSerializer
    queryset = Placar.objects.all()