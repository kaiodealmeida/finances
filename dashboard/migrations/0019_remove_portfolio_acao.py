# Generated by Django 3.2.7 on 2021-09-28 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20210928_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='acao',
        ),
    ]
