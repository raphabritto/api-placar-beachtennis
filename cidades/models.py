from django.db import models

# Create your models here.

def upload_bandeira_estado(instance, nome_arquivo):
    return f'estados/{instance.nome}-{nome_arquivo}'

def upload_bandeira_pais(instance, nome_arquivo):
    return f'paises/{instance.nome}-{nome_arquivo}'


class Paises(models.Model):
    pais_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    bandeira = models.ImageField(upload_to=upload_bandeira_pais, blank=True, null=True)
    data_inclusao = models.DateTimeField(auto_now_add=True, null=False)
    data_ultima_modificacao = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.nome


class Estados(models.Model):
    estado_id = models.AutoField(primary_key=True)
    pais = models.ForeignKey(Paises, on_delete=models.RESTRICT)
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    bandeira = models.ImageField(upload_to=upload_bandeira_estado, null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True, null=False)
    data_ultima_modificacao = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.nome


class Cidades(models.Model):
    cidade_id = models.AutoField(primary_key=True)
    estado = models.ForeignKey(Estados, on_delete=models.RESTRICT)
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    data_inclusao = models.DateTimeField(auto_now_add=True, null=False)
    data_ultima_modificacao = models.DateTimeField(auto_now_add=True, null=False)
        