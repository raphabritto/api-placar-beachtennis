from rest_framework import serializers

from .models import Paises, Estados, Cidades


class PaisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paises
        fields = '__all__'


class EstadosSerializer(serializers.ModelSerializer):
    pais = PaisesSerializer()

    class Meta:
        model = Estados
        fields = '__all__'


class CidadesSerializer(serializers.ModelSerializer):
    estado = EstadosSerializer()
    
    class Meta:
        model = Cidades
        fields = '__all__'