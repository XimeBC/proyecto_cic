# Generated by Django 3.1.7 on 2021-03-01 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0003_auto_20210226_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control_usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.CharField(max_length=200)),
                ('oxigeno', models.CharField(max_length=200)),
                ('fecha_hora_registro', models.CharField(max_length=200)),
            ],
        ),
    ]