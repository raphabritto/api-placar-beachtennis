from datetime import datetime

from django.core.serializers import serialize
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import add_query_param

from .models import *
from .serializers import *


class PaisesViewSet(viewsets.ModelViewSet):
    serializer_class = PaisesSerializer
    queryset = Paises.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class EstadosViewSet(viewsets.ModelViewSet):
    serializer_class = EstadosSerializer
    queryset = Estados.objects.all()

    # def get_queryset(self):
    #     pais = self.request.query_params.get('pais', None)

    #     queryset = Estados.objects.all()

    #     if pais:
    #         queryset = queryset.filter(pais=pais)

    #     return queryset


class CidadesViewSet(viewsets.ModelViewSet):
    serializer_class = CidadesSerializer
    queryset = Cidades.objects.all()

    # def get_queryset(self):
    #     estado = self.request.query_params.get('estado', None)
    #     queryset = Cidades.objects.all()

    #     if estado:
    #         queryset = queryset.filter(estado=estado)

    #     return queryset
