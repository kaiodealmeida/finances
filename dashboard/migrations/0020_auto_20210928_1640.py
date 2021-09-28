# Generated by Django 3.2.7 on 2021-09-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_remove_portfolio_acao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acoes',
            name='adjclose',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='acoes',
            name='retorno',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='acoes',
            name='ticker',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='acoes',
            name='txrisk',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='adjclose',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='retorno',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='ticker',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='txrisk',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]