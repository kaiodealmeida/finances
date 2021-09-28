from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Acoes(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    investidor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True)
    ticker = models.CharField(max_length=7)
    adjclose = models.DecimalField(max_digits=7, decimal_places=2)
    retorno = models.DecimalField(max_digits=7, decimal_places=2)
    txrisk = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.ticker

