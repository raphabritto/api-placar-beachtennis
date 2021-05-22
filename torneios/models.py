from uuid import uuid4

from django.db import models

from atletas.models import Atletas
from cidades.models import Cidades

# Create your models here.

def upload_panfleto_torneio(instance, nome_arquivo):
    return f'torneios/{instance.torneio_id}-{nome_arquivo}'

class Torneios(models.Model):
    torneio_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    data_inicio_inscricao = models.DateField()
    data_termino_inscricao = models.DateField()
    data_inicio_torneio = models.DateField()
    data_termino_torneio = models.DateField()
    cidade = models.ForeignKey(Cidades, on_delete=models.RESTRICT)
    local = models.CharField(max_length=80)
    endereco = models.CharField(max_length=120)
    responsavel = models.CharField(max_length=60)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    informacao = models.TextField(max_length=1000, null=True)
    panfleto = models.ImageField(upload_to=upload_panfleto_torneio, blank=True, null=True)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    data_ultima_modificacao = models.DateTimeField(auto_now_add=True)


class Categorias(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    # torneio = models.ForeignKey(Torneios, on_delete=models.RESTRICT)
    nome =  models.CharField(max_length=60)
    ativa = models.BooleanField(default=True)
    idade_minima = models.SmallIntegerField()
    idade_maxima = models.SmallIntegerField()
    numero_atletas = models.SmallIntegerField()
    data_inclusao = models.DateTimeField(auto_now_add=True)
    data_ultima_modificacao = models.DateTimeField(auto_now_add=True)


class TorneioCategorias(models.Model):
    torneio = models.ForeignKey(Torneios, on_delete=models.RESTRICT)
    categoria = models.ForeignKey(Categorias, on_delete=models.RESTRICT)
    numero_inscricao = models.SmallIntegerField()


class Equipes(models.Model):
    equipe_id = models.IntegerField()
    torneio = models.ForeignKey(Torneios, on_delete=models.RESTRICT)
    categoria = models.ForeignKey(Categorias, on_delete=models.RESTRICT)
    atleta = models.ForeignKey(Atletas, on_delete=models.RESTRICT)


class Jogos(models.Model):
    jogo_id = models.UUIDField(primary_key=True, default=uuid4)
    torneio = models.ForeignKey(Torneios, on_delete=models.RESTRICT)
    data_jogo = models.DateField()
    hora_jogo = models.TimeField()
    # quadra


class jogoEquipes(models.Model):
    jogo = models.ForeignKey(Jogos, on_delete=models.RESTRICT)
    equipe = models.ForeignKey(Equipes, on_delete=models.RESTRICT)
