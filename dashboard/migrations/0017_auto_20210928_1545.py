# Generated by Django 3.2.7 on 2021-09-28 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_alter_portfolio_ticker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='investidor',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='acoes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.acoes'),
        ),
    ]
