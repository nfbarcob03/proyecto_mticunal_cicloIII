# Generated by Django 4.1.1 on 2022-09-14 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_casa_app', '0003_rename_usuario_paciente_id_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='create_date',
            field=models.DateField(null=True, verbose_name='create_date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_date',
            field=models.DateField(null=True, verbose_name='create_date'),
        ),
    ]