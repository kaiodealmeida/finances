# Generated by Django 3.2.7 on 2021-09-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20210928_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='ticker',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
