from django.db.models import fields
from rest_framework import serializers

# from .models import Torneios, NivelCategorias, GeneroCategorias
from .models import *

from datetime import datetime


class TorneiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneios
        fields = '__all__'

    
    # def validate(self, data):
    #     if data['dataTerminoTorneio'] < data['dataInicioTorneio']:
    #         raise serializers.ValidationError("Data Termino não pode ser menor que Data Inicio")
    
    #     return data


class NivelCategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelCategorias
        fields = '__all__'


    def create(self, validated_data):
        nivelCategoria = NivelCategorias.objects.create(
            nomeNivel = validated_data['nomeNivel'].upper(),
            idadeMinima = validated_data['idadeMinima'],
            idadeMaxima = validated_data['idadeMaxima'],
            ativo = validated_data['ativo'],
            dataInclusao = datetime.now(),
            dataAtualizacao = datetime.now()
        )
        nivelCategoria.save()

        return nivelCategoria


    def update(self, instance, validated_data):
        instance.nomeNivel = validated_data['nomeNivel'].upper()
        instance.idadeMinima = validated_data['idadeMinima']
        instance.idadeMaxima = validated_data['idadeMaxima']
        instance.ativo = validated_data['ativo']
        instance.dataAtualizacao = datetime.now()
        instance.save()

        return instance


class GeneroCategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroCategorias
        fields = '__all__'

    def create(self, validated_data):
        generoCategoria = GeneroCategorias.objects.create(
            nomeGenero=validated_data['nomeGenero'].upper(),
            ativo=validated_data['ativo'],
            dataInclusao=datetime.now(),
            dataAtualizacao=datetime.now()
        )
        generoCategoria.save()

        return generoCategoria


    def update(self, instance, validated_data):
        instance.nomeGenero = validated_data['nomeGenero'].upper()
        instance.ativo = validated_data['ativo']
        instance.dataAtualizacao = datetime.now()
        instance.save()

        return instance


class TipoCategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCategorias
        fields = '__all__'

    def create(self, validated_data):
        tipoCategoria = TipoCategorias.objects.create(
            nomeTipo = validated_data['nomeTipo'].upper(),
            quantidadeAtletas = validated_data['quantidadeAtletas'],
            ativo = validated_data['ativo'],
            dataInclusao = datetime.now(),
            dataAtualizacao=datetime.now()
        )
        tipoCategoria.save()

        return tipoCategoria

    def update(self, instance, validated_data):
        instance.nomeTipo = validated_data['nomeTipo'].upper()
        instance.quantidadeAtletas = validated_data['quantidadeAtletas']
        instance.ativo = validated_data['ativo']
        instance.dataAtualizacao = datetime.now()
        instance.save()

        return instance


class TorneioCategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TorneioCategorias
        fields = '__all__'

    def create(self, validated_data):
        torneioCategoria = TorneioCategorias.objects.create(
            torneio = Torneios.objects.get(torneioId = validate_data['torneioId']),
            tipoCategoria = TipoCategorias.objects.get(tipoId = validate_data['tipoId']),
            # generoCategoria = models.ForeignKey(GeneroCategorias),
            # nivelCategoria = models.ForeignKey(NivelCategorias),
            numeroMaximoParticipantes = validate_data['numeroMaximoParticipantes'],
            ativo = validated_data['ativo'],
            dataInclusao = datetime.now(),
            dataAtualizacao = datetime.now()

            # try:
            #     pais = Paises.objects.get(pais_id=data['pais'])
            #     instance.pais = pais
            # except KeyError:
            #     pass

        )
        torneioCategoria.save()

        return torneioCategoria

    # def update(self, instance, validated_data):
    #     instance.nomeTipo = validated_data['nomeTipo'].upper()
    #     instance.quantidadeAtletas = validated_data['quantidadeAtletas']
    #     instance.ativo = validated_data['ativo']
    #     instance.dataAtualizacao = datetime.now()
    #     instance.save()

    #     return instance
