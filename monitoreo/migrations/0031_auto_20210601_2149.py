# Generated by Django 3.1.7 on 2021-06-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0030_auto_20210529_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restringidos',
            name='tipo_prueba',
            field=models.IntegerField(default=0),
        ),
    ]
