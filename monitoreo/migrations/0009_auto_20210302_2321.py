# Generated by Django 3.1.7 on 2021-03-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0008_auto_20210228_2127'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registro',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_nacimiento',
            field=models.DateField(max_length=200),
        ),
    ]
