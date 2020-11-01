# Generated by Django 3.1.1 on 2020-10-23 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nro_doc', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tipo_doc', models.CharField(max_length=20)),
                ('nombre_completo', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField(max_length=20)),
                ('genero', models.CharField(max_length=20)),
                ('telefono', models.IntegerField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('contraseña', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=250)),
                ('ofertas', models.BooleanField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=100)),
                ('cod_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Porciones',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.CharField(max_length=50)),
                ('precio', models.FloatField(max_length=20)),
                ('cod_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fec_ing', models.DateField(max_length=20)),
                ('direccion', models.CharField(max_length=250)),
                ('fec_entrega', models.DateField(max_length=20)),
                ('hora_entrega', models.CharField(max_length=10)),
                ('telefono', models.IntegerField(max_length=12)),
                ('nombre_completo', models.CharField(max_length=50)),
                ('cod_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField(max_length=20)),
                ('cod_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
                ('cod_porciones', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.porciones')),
                ('cod_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
        ),
    ]
