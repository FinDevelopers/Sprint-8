# Generated by Django 4.0.6 on 2022-08-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0020_alter_empleado_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address_street', models.TextField()),
                ('address_number', models.TextField()),
                ('address_city', models.TextField()),
                ('address_province', models.TextField()),
                ('address_country', models.TextField()),
                ('address_customer', models.IntegerField(blank=True, null=True)),
                ('address_employee', models.IntegerField(blank=True, null=True)),
                ('address_branch', models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
    ]