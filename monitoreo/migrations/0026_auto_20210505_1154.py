# Generated by Django 3.1.7 on 2021-05-05 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitoreo', '0025_auto_20210504_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='restringidos',
            name='nombre_usuario',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='control_usuarios',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='qrs',
            name='url',
            field=models.ImageField(blank=True, unique=True, upload_to='qr_codes'),
        ),
        migrations.AlterField(
            model_name='restringidos',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='boleta',
            field=models.CharField(default='Invitado', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='curp',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.CharField(default='NULL', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre_usuario',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
