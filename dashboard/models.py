from django.db import models
from django.utils import timezone

# Create your models here.


class Investidor(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now)


class Acoes(models.Model):
    ticker = models.CharField(max_length=10)
    adjclose = models.DecimalField(max_digits=19, decimal_places=16)
    returntx = models.DecimalField(max_digits=19, decimal_places=16)
    risktx = models.DecimalField(max_digits=19, decimal_places=16)


class Portfolio(models.Model):
    investidor = models.ForeignKey(
        Investidor, on_delete=models.DO_NOTHING, null=True)
    acoes = models.ForeignKey(Acoes, on_delete=models.DO_NOTHING, null=True)
