from django.db import models

# Create your models here.

# def upload_bandeira_pais(instance, nome_arquivo):
#     return f'paises/{instance.nome}-{nome_arquivo}'


# class Paises(models.Model):
#     pais_id = models.AutoField(primary_key=True)
#     nome = models.CharField(max_length=100)
#     bandeira = models.ImageField(upload_to=upload_bandeira_pais, blank=True, null=True)
#     data_inclusao = models.DateTimeField(auto_now_add=True, null=False)
#     data_ultima_modificacao = models.DateTimeField(auto_now_add=True, null=False)

#     def __str__(self):
#         return self.nome