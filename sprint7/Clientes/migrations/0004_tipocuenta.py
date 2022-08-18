# Generated by Django 4.0.6 on 2022-08-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_alter_cliente_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('act_id', models.AutoField(primary_key=True, serialize=False)),
                ('act_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipo_cuenta',
                'managed': False,
            },
        ),
    ]
