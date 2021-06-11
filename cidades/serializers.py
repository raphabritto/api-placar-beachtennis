from rest_framework import serializers

from .models import *


class PaisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paises
        fields = '__all__'

    def create(self, validate_data):
        # data = request.data

        pais = Paises.objects.create(
            nomePais = validate_data['nomePais'].upper(),
            siglaPais = validate_data['siglaPais'].upper()
        )
        pais.save()

        return pais

    def update(self, instance, validate_data):
        instance.nomePais = validate_data['nomePais'].upper()
        instance.siglaPais = validate_data['siglaPais'].upper()
        # instance.bandeira = data.get('bandeira', None)
        # instance.data_ultima_modificacao = datetime.now()
        instance.save()

        return instance

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     data = request.data

    #     instance.nome = data.get('nome', instance.nome).upper()
    #     instance.sigla = data.get('sigla', instance.sigla).upper()
    #     instance.bandeira = data.get('bandeira', instance.bandeira)
    #     instance.data_ultima_modificacao = datetime.now()
    #     instance.save()
    #     serializer = PaisesSerializer(instance)

    #     return Response(serializer.data)


class EstadosSerializer(serializers.ModelSerializer):
    # pais = PaisesSerializer()

    class Meta:
        model = Estados
        fields = '__all__'

    def create(self, validate_data):
        # pais = Pais.objects.get(paisId = validate_data['pais'])
        pais = validate_data.pop('pais')
        estado = Estados.objects.create(
            pais = pais,
            nomeEstado = validate_data['nomeEstado'].upper(),
            siglaEstado = validate_data['siglaEstado'].upper()
        )
        estado.save()

        return estado

    def update(self, instance, validate_data):
        # pais = Paises.objects.get(paisId = validate_data['pais'])
        pais = validate_data.pop('pais')
        instance.pais = pais
        instance.nomeEstado = validate_data.get('nomeEstado', instance.nomeEstado).upper()
        instance.siglaEstado = validate_data.get('siglaEstado', instance.siglaEstado).upper()
        # object.bandeira = [field if field is not None else object.bandeira for field in data['bandeira']]
        instance.save()

        return instance

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     data = request.data

    #     try:
    #         pais = Paises.objects.get(pais_id=data['pais'])
    #         instance.pais = pais
    #     except KeyError:
    #         pass

    #     instance.nome = data.get('nome', instance.nome).upper()
    #     instance.sigla = data.get('sigla', instance.sigla).upper()
    #     instance.data_ultima_modificacao = datetime.now()
    #     instance.save()
    #     serializer = EstadosSerializer(instance)

    #     return Response(serializer.data)


class CidadesSerializer(serializers.ModelSerializer):
    # estado = EstadosSerializer()
    
    class Meta:
        model = Cidades
        fields = '__all__'

    def create(self, validate_data):
        # estado = Estados.objects.get(estadoId = validate_data['estado'])
        estado = validate_data.pop('estado')
        cidade = Cidades.objects.create(
            estado = estado,
            nomeCidade = validate_data.get('nomeCidade').upper()
        )
        cidade.save()

        return cidade

    def update(self, instance, validate_data):
        estado = validate_data.pop('estado')
        instance.estado = estado
        instance.nomeCidade = validate_data.get('nomeCidade', instance.nomeCidade).upper()
        instance.save()
        
        return instance

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     data = request.data

    #     try:
    #         estado = Estados.objects.get(estado_id=data['estado'])
    #         instance.estado = estado
    #     except KeyError:
    #         pass

    #     instance.nome = data.get('nome', instance.nome).upper()
    #     instance.sigla = data.get('sigla', instance.sigla).upper()
    #     instance.data_ultima_modificacao = datetime.now()

    #     instance.save()
    #     serializer = CidadesSerializer(instance)

    #     return Response(serializer.data)
