# Generated by Django 3.1.7 on 2021-04-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0013_auto_20210402_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='id_tipo',
            field=models.IntegerField(choices=[(1, 'Estudiante'), (2, 'Docente'), (3, 'Administrador'), (4, 'Invitado')], default=1),
        ),
        migrations.AlterField(
            model_name='salones',
            name='estado',
            field=models.IntegerField(),
        ),
    ]