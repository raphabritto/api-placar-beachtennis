from datetime import datetime

from django.core.serializers import serialize
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import add_query_param

from .models import Cidades, Estados, Paises
from .serializers import CidadesSerializer, EstadosSerializer, PaisesSerializer


class PaisesViewSet(viewsets.ModelViewSet):
    serializer_class = PaisesSerializer
    queryset = Paises.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        data = request.data

        pais = Paises.objects.create(nome=data['nome'].upper(), sigla=data['sigla'].upper(), bandeira=data['bandeira'])
        pais.save()
        serializer = PaisesSerializer(pais)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        instance.nome = data['nome'].upper()
        instance.sigla = data['sigla'].upper()
        instance.bandeira = data.get('bandeira', None)
        instance.data_ultima_modificacao = datetime.now()
        instance.save()
        serializer = PaisesSerializer(instance)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        instance.nome = data.get('nome', instance.nome).upper()
        instance.sigla = data.get('sigla', instance.sigla).upper()
        instance.bandeira = data.get('bandeira', instance.bandeira)
        instance.data_ultima_modificacao = datetime.now()
        instance.save()
        serializer = PaisesSerializer(instance)

        return Response(serializer.data)
 

class EstadosViewSet(viewsets.ModelViewSet):
    serializer_class = EstadosSerializer
    queryset = Estados.objects.all()

    def get_queryset(self):
        pais = self.request.query_params.get('pais', None)

        queryset = Estados.objects.all()

        if pais:
            queryset = queryset.filter(pais=pais)

        return queryset
        

    def create(self, request, *args, **kwargs):
        data = request.data
        # data_insert = datetime.now()
        pais = Pais.objects.get(pais_id=data['pais'])
        estado = Estado.objects.create(nome=data['nome'].upper(), sigla=data['sigla'].upper(), pais=pais)
        estado.save()
        serializer = EstadosSerializer(estado)

        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        pais = Paises.objects.get(pais_id=data['pais'])
        instance.pais = pais
        instance.nome = data['nome'].upper()
        instance.sigla = data['sigla'].upper()
        # object.bandeira = [field if field is not None else object.bandeira for field in data['bandeira']]
        instance.data_ultima_modificacao = datetime.now()
        instance.save()
        serializer = EstadosSerializer(instance)
        
        return Response(serializer.data)


    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        try:
            pais = Paises.objects.get(pais_id=data['pais'])
            instance.pais = pais
        except KeyError:
            pass

        instance.nome = data.get('nome', instance.nome).upper()
        instance.sigla = data.get('sigla', instance.sigla).upper()
        instance.data_ultima_modificacao = datetime.now()
        instance.save()
        serializer = EstadosSerializer(instance)

        return Response(serializer.data)


class CidadesViewSet(viewsets.ModelViewSet):
    serializer_class = CidadesSerializer
    # queryset = Cidades.objects.all()

    def get_queryset(self):
        estado = self.request.query_params.get('estado', None)
        queryset = Cidades.objects.all()

        if estado:
            queryset = queryset.filter(estado=estado)

        return queryset


    def create(self, request, *args, **kwargs):
        data = request.data
        estado = Estados.objects.get(estado_id=data['estado'])
        cidade = Cidades.objects.create(nome=data['nome'].upper(), sigla=data['sigla'].upper())
        cidade.save()
        serializer = CidadesSerializer(cidade)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        estado = Estados.objects.get(estado_id=data['estado'])
        instance.estado = estado
        instance.nome = data['nome'].upper()
        instance.sigla = data['sigla'].upper()
        instance.data_ultima_modificacao = datetime.now()
        instance.save()
        serializer = CidadesSerializer(instance)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        try:
            estado = Estados.objects.get(estado_id=data['estado'])
            instance.estado = estado
        except KeyError:
            pass

        instance.nome = data.get('nome', instance.nome).upper()
        instance.sigla = data.get('sigla', instance.sigla).upper()
        instance.data_ultima_modificacao = datetime.now()

        instance.save()
        serializer = CidadesSerializer(instance)

        return Response(serializer.data)
