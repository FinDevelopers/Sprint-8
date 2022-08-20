# Generated by Django 4.0.6 on 2022-08-13 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0023_alter_direccion_address_branch_and_more'),
        ('Cuentas', '0004_alter_cuenta_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuenta',
            options={'managed': True, 'ordering': ['account_id'], 'verbose_name': 'Cuenta', 'verbose_name_plural': 'Cuentas'},
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='account_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='account_type',
            field=models.ForeignKey(db_column='account_type', on_delete=django.db.models.deletion.DO_NOTHING, related_name='cuentas', to='Cuentas.tipocuenta', verbose_name='Tipo de Cuenta'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='balance',
            field=models.IntegerField(verbose_name='balance'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuentas', to='Clientes.cliente', verbose_name='usuario'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='iban',
            field=models.TextField(verbose_name='Código Internacional de Cuentas Bancarias'),
        ),
    ]