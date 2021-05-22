# from builtins import object
# from datetime import datetime

from django.core.serializers import serialize
from rest_framework import serializers, viewsets
from rest_framework.response import Response

# from .models import Estados
# from .serializers import EstadosSerializer
# from paises.models import Paises


# class EstadosViewSet(viewsets.ModelViewSet):
#     serializer_class = EstadosSerializer
#     queryset = Estados.objects.all()


#     def update(self, request, *args, **kwargs):
#         object = self.get_object()
#         data = request.data
#         pais = Paises.objects.get(pais_id=data['pais'])
#         object.pais = pais
#         object.nome = data['nome']
#         object.sigla = data['sigla']
#         # object.bandeira = [field if field is not None else object.bandeira for field in data['bandeira']]
#         object.data_ultima_modificacao = datetime.now()
#         object.save()
#         serializer = EstadosSerializer(object)
        
#         return Response(serializer.data)

#     def partial_update(self, request, *args, **kwargs):
#         object = self.get_object()
#         data = request.data

#         try:
#             pais = Paises.objects.get(pais_id=data['pais'])
#             object.pais = pais
#         except KeyError:
#             pass

#         object.nome = data.get('nome', object.nome)
#         object.sigla = data.get('sigla', object.sigla)
#         object.data_ultima_modificacao = datetime.now()
#         object.save()

#         serializer = EstadosSerializer(object)

#         return Response(serializer.data)