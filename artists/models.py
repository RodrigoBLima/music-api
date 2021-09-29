from django.db import models
from datetime import datetime,

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=80, blank=False,
                            verbose_name="Nome do artista")
    artistic_name = models.CharField(max_length=80, blank=False,
                                     verbose_name="Nome artístico")
    cpf = models.CharField(
        max_length=14, verbose_name="CPF", blank=True, unique=True)
    rg = models.CharField(max_length=12, verbose_name="RG",
                          blank=True, unique=True)
    created_at = models.DateTimeField(
        default=datetime.now, verbose_name="Data de criação")
