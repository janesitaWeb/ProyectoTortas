# Generated by Django 3.1.1 on 2020-11-02 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201024_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='telefono',
        ),
    ]
