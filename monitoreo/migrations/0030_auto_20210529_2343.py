# Generated by Django 3.1.7 on 2021-05-30 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0029_auto_20210507_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restringidos',
            name='tipo_prueba',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tipos_usuario',
            name='descripcion',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tipos_usuario',
            name='estado',
            field=models.IntegerField(default=1),
        ),
    ]
