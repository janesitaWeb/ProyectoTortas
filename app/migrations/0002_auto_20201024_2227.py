# Generated by Django 3.1.1 on 2020-10-25 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='contraseña',
            new_name='pasword',
        ),
    ]
