from django.db import models

# Create your models here.


class Calculos(models.Model):
    ticker = models.CharField(max_length=10)
    adjclose = models.DecimalField(max_digits=19, decimal_places=16)
    returntx = models.DecimalField(max_digits=19, decimal_places=16)
    risktx = models.DecimalField(max_digits=19, decimal_places=16)
