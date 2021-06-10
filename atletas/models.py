from uuid import uuid4

from django.db import models
# from rest_framework.fields import RegexField

# from datetime import date
from cidades.models import Cidades

# Create your models here.

def upload_foto_atleta(instance, nome_arquivo):
    return f'atletas/{instance.atleta_id}-{nome_arquivo}'


class Atletas(models.Model):
    # atleta_id = models.IntegerField(primary_key=True, editable=False)
    atleta_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cidade = models.ForeignKey(Cidades, on_delete=models.RESTRICT)
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    apelido = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    # cpf = models.RegexField(regex=r'\d', max_length=11, unique=True)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to=upload_foto_atleta, blank=True, null=True)
    ativo = models.BooleanField(default=False)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.nome

    # @property
    # def idade(self):
    #     return int((date.today() - self.data_nascimento).days / 365.2425)