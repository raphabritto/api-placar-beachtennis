from uuid import uuid4

from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, SmallIntegerField

from atletas.models import Atletas
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

    def __str__(self):
        return self.nomeTorneio


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

    def __str__(self):
        return self.nomeGenero


class NivelCategorias(models.Model):
    # nivelId = models.SmallIntegerField(primary_key=True, editable=False)
    nivelId = models.AutoField(primary_key=True)
    nomeNivel = models.CharField(max_length=20)
    idadeMinima = models.SmallIntegerField()
    idadeMaxima = models.SmallIntegerField()
    ativo = models.BooleanField(default=True)
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomeNivel


class TipoCategorias(models.Model):
    tipoId = models.AutoField(primary_key=True)
    nomeTipo = models.CharField(max_length=50)
    quantidadeAtletas = models.SmallIntegerField()
    ativo = models.BooleanField(default=True)
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomeTipo

    # class Meta:
    #     verbose_name = 'Tipo Categoria'
    #     verbose_name_plural = 'Tipo Categorias'


# class Categorias(models.Model):
#     categoriaId = models.SmallIntegerField(primary_key=True, editable=False)
#     nomeCategoria = models.CharField(max_length=100)
#     ativo = models.BooleanField(default=True)
#     dataInclusao = models.DateTimeField(auto_now_add=True)
#     dataAtualizacao = models.DateTimeField(auto_now_add=True)


class TorneioCategorias(models.Model):
    torneioCategoriaId = models.AutoField(primary_key=True)
    torneio = models.ForeignKey(Torneios, on_delete=models.RESTRICT)
    tipoCategoria = models.ForeignKey(TipoCategorias, on_delete=models.RESTRICT, verbose_name='Tipo Categoria')
    generoCategoria = models.ForeignKey(GeneroCategorias, on_delete=models.RESTRICT, verbose_name='Genero')
    nivelCategoria = models.ForeignKey(NivelCategorias, on_delete=models.RESTRICT, verbose_name='Nivel')
    # idadeMinima = models.SmallIntegerField()
    # idadeMaxima = models.SmallIntegerField()
    numeroMaximoParticipantes = models.SmallIntegerField(verbose_name='Numero Maximo Participantes/Duplas')
    ativo = models.BooleanField(default=True)
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)

    # def validate_unique(self, exclude: None):
    #     torneio = Torneios.objects.filter(torneioId = self.torneio.torneioId)
    #     if self.pk is None:
    #         if torneio.filter(item = self.item).exists():
    #             raise ValidationError('item ja existe')

    #     return super().validate_unique(exclude=exclude)

    class Meta:
        unique_together = ('torneio', 'tipoCategoria', 'generoCategoria', 'nivelCategoria')
        # managed = False
        # db_table = tor
        # verbose_name = 'Categoria'
        # verbose_name_plural = 'Categorias'

        # constraints = [
        #     models.UniqueConstraint(fields=['torneio', 'tipoCategoria', 'generoCategoria', 'nivelCategoria'], name='categoria_torneio_unica')
        # ]


class Equipes(models.Model):
    equipeId = models.AutoField(primary_key=True)
    torneioCategoria = models.ForeignKey(TorneioCategorias, on_delete=models.RESTRICT)
    atleta = models.ManyToManyField(Atletas, related_name='atletas', verbose_name='Atleta(s)')
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)


# class Grupos(models.Model):
#     grupoId = models.AutoField(primary_key=True)
#     equipes = models.ManyToManyField
#     dataInclusao = models.DateTimeField(auto_now_add=True)
#     dataAtualizacao = models.DateTimeField(auto_now_add=True)


class Jogos(models.Model):
    # jogoId = models.UUIDField(primary_key=True, default=uuid4)
    jogoId = models.AutoField(primary_key=True)
    equipeA = models.ForeignKey(Equipes, on_delete=models.RESTRICT, related_name='equipeA')
    equipeB = models.ForeignKey(Equipes, on_delete=models.RESTRICT, related_name='equipeB')
    dataJogo = models.DateField()
    horaJogo = models.TimeField()
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)


class Placar(models.Model):
    placarId = models.AutoField(primary_key=True)
    jogo = models.ForeignKey(Jogos, on_delete=models.RESTRICT)
    equipe = models.ForeignKey(Equipes, on_delete=models.RESTRICT)
    numeroSet = models.IntegerField()
    numeroGame = models.IntegerField()
    dataInclusao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now_add=True)

# class jogoEquipes(models.Model):
#     jogo = models.ForeignKey(Jogos, on_delete=models.RESTRICT)
#     equipe = models.ForeignKey(Equipes, on_delete=models.RESTRICT)
