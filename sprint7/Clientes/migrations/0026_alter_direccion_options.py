# Generated by Django 4.0.6 on 2022-08-15 19:14

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0025_alter_direccion_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direccion',
            options={'managed': True, 'ordering': ['address_id'], 'verbose_name': 'Dirección', 'verbose_name_plural': 'Direcciones'},
        ),
    ]
