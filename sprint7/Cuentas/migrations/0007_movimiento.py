# Generated by Django 4.0.6 on 2022-08-14 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0025_alter_direccion_options'),
        ('Cuentas', '0006_alter_cuenta_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('movement_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_total', models.IntegerField(verbose_name='monto')),
                ('movement_type', models.TextField(choices=[('transf_recib', 'Transferencia Recibida'), ('transf_env', 'Transferencia Enviada'), ('efectivo_ing', 'Ingreso Efectivo'), ('efectivo_eg', 'Egreso Efectivo')], verbose_name='tipo')),
                ('movement_datetime', models.DateTimeField(auto_now_add=True, verbose_name='fecha')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='Clientes.cliente', verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
                'db_table': 'movimientos',
                'ordering': ['movement_id'],
                'managed': True,
            },
        ),
    ]