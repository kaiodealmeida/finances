# Generated by Django 3.2.7 on 2021-09-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210927_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acoes',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]