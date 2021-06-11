from django.db import models

# Create your models here.

def upload_bandeira_estado(instance, nome_arquivo):
    return f'estados/{instance.nome}-{nome_arquivo}'

def upload_bandeira_pais(instance, nome_arquivo):
    return f'paises/{instance.nome}-{nome_arquivo}'


class Paises(models.Model):
    paisId = models.AutoField(primary_key=True)
    nomePais = models.CharField(max_length=100)
    siglaPais = models.CharField(max_length=3)
    # bandeiraPais = models.ImageField(upload_to=upload_bandeira_pais, blank=True, null=True)
    # data_inclusao = models.DateTimeField(auto_now_add=True, null=False)
    # data_ultima_modificacao = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.nomePais


class Estados(models.Model):
    estadoId = models.AutoField(primary_key=True)
    pais = models.ForeignKey(Paises, on_delete=models.RESTRICT)
    nomeEstado = models.CharField(max_length=50)
    siglaEstado = models.CharField(max_length=2)
    # bandeira = models.ImageField(upload_to=upload_bandeira_estado, null=True, blank=True)
    # data_inclusao = models.DateTimeField(auto_now_add=True, null=False)
    # data_ultima_modificacao = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.nomeEstado


class Cidades(models.Model):
    cidadeId = models.AutoField(primary_key=True)
    estado = models.ForeignKey(Estados, on_delete=models.RESTRICT)
    nomeCidade = models.CharField(max_length=100)
    # siglaCidade = models.CharField(max_length=3)
    # data_inclusao = models.DateTimeField(auto_now_add=True, null=False)
    # data_ultima_modificacao = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.nomeCidade
