# Generated by Django 3.1.7 on 2021-05-06 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0027_restringidos_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restringidos',
            name='estado',
        ),
    ]