# Generated by Django 4.1.1 on 2022-09-14 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_casa_app', '0002_remove_familiar_id_usuario_remove_medico_id_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='usuario',
            new_name='id_usuario',
        ),
    ]