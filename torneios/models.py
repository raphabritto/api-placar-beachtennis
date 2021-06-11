from uuid import uuid4

from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, SmallIntegerField

# from atletas.models import Atletas
from cidades.models import Cidades

# Create your models here.

def upload_panfleto_torneio(instance, nome_arquivo):
    return f'torneios/{instance.torneio_id}-{nome_arquivo}'

class Torneios(models.Model):
    torneioId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nomeTorneio = models.CharField(max_length=100)
    # dataInicioInscricao = models.DateField()
    # dataTerminoInscricao = models.DateField()
    # dataInicioTorneio = models.DateField()
    # dataTerminoTorneio = models.DateField()
    # cidade = models.ForeignKey(Cidades, on_delete=models.RESTRICT)
    # local = models.CharField(max_length=80)
    # endereco = models.CharField(max_length=120)
    # responsavel = models.CharField(max_length=60)
    # telefone = models.CharField(max_length=20)
    # email = models.EmailField(max_length=100)
    # informacao = models.TextField(max_length=1000, null=True)
    # panfleto = models.ImageField(upload_to=upload_panfleto_torneio, blank=True, null=True)
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)

# sexo_dic = ({"id": 1, "value": "Feminino"}, 
#             {"id": 2, "value": "Masculino"}, 
#             {"id": 3, "value": "Mista"})
# sexo = [item for item in sexo_dic]


class GeneroCategorias(models.Model):
    # generoId = models.SmallIntegerField(primary_key=True, editable=False)
    generoId = models.AutoField(primary_key=True)
    nomeGenero = models.CharField(max_length=40)
    # somenteDuplas = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)


class NivelCategorias(models.Model):
    # nivelId = models.SmallIntegerField(primary_key=True, editable=False)
    nivelId = models.AutoField(primary_key=True)
    nomeNivel = models.CharField(max_length=20)
    idadeMinima = models.SmallIntegerField()
    idadeMaxima = models.SmallIntegerField()
    ativo = models.BooleanField(default=True)
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)


class TipoCategorias(models.Model):
    tipoId = models.AutoField(primary_key=True)
    nomeTipo = models.CharField(max_length=50)
    quantidadeAtletas = models.SmallIntegerField()
    ativo = models.BooleanField(default=True)
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)


# class Categorias(models.Model):
#     categoriaId = models.SmallIntegerField(primary_key=True, editable=False)
#     nomeCategoria = models.CharField(max_length=100)
#     ativo = models.BooleanField(default=True)
#     dataInclusao = models.DateTimeField(auto_now_add=True)
#     dataAtualizacao = models.DateTimeField(auto_now_add=True)


class TorneioCategorias(models.Model):
    torneio = models.ForeignKey(Torneios, on_delete=models.RESTRICT)
    tipoCategoria = models.ForeignKey(TipoCategorias, on_delete=models.RESTRICT)
    generoCategoria = models.ForeignKey(GeneroCategorias, on_delete=models.RESTRICT)
    nivelCategoria = models.ForeignKey(NivelCategorias, on_delete=models.RESTRICT)
    # idadeMinima = models.SmallIntegerField()
    # idadeMaxima = models.SmallIntegerField()
    numeroMaximoParticipantes = models.SmallIntegerField()
    ativo = models.BooleanField(default=True)
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)


# class Equipes(models.Model):
#     equipe_id = models.IntegerField()
#     torneio = models.ForeignKey(Torneios, on_delete=models.RESTRICT)
#     # categoria = models.ForeignKey(Categorias, on_delete=models.RESTRICT)
#     atleta = models.ForeignKey(Atletas, on_delete=models.RESTRICT)


# class Jogos(models.Model):
#     jogo_id = models.UUIDField(primary_key=True, default=uuid4)
#     torneio = models.ForeignKey(Torneios, on_delete=models.RESTRICT)
#     data_jogo = models.DateField()
#     hora_jogo = models.TimeField()
#     # quadra


# class jogoEquipes(models.Model):
#     jogo = models.ForeignKey(Jogos, on_delete=models.RESTRICT)
#     equipe = models.ForeignKey(Equipes, on_delete=models.RESTRICT)
