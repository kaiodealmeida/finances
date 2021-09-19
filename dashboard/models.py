from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Acoes(models.Model):
    investidor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True)
    ticker = models.CharField(max_length=10, unique=True)
    adjclose = models.DecimalField(max_digits=190, decimal_places=160)
    retorno = models.DecimalField(max_digits=190, decimal_places=160)
    txrisk = models.DecimalField(max_digits=190, decimal_places=160)

    def __str__(self):
        return self.ticker
