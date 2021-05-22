from django.db import models
# from paises.models import Paises

# Create your models here.

# def upload_bandeira_estado(instance, nome_arquivo):
#     return f'estados/{instance.nome}-{nome_arquivo}'

# class Estados(models.Model):
#     estado_id = models.AutoField(primary_key=True)
#     pais = models.ForeignKey(Paises, on_delete=models.RESTRICT)
#     nome = models.CharField(max_length=50)
#     sigla = models.CharField(max_length=2)
#     bandeira = models.ImageField(upload_to=upload_bandeira_estado, null=True, blank=True)
#     data_inclusao = models.DateTimeField(auto_now_add=True, null=False)
#     data_ultima_modificacao = models.DateTimeField(auto_now_add=True, null=False)

#     def __str__(self):
#         return self.nome