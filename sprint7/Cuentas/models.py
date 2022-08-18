from django.db import models
from Clientes.models import Cliente

# Create your models here.
class TipoCuenta(models.Model):
    act_id = models.AutoField(primary_key=True, verbose_name='ID')
    act_name = models.TextField(blank=True, null=True, verbose_name='nombre')

    def __str__(self):
        return self.act_name

    class Meta:
        managed = True
        db_table = 'tipo_cuenta'
        verbose_name = 'Tipo de Cuenta'
        verbose_name_plural = 'Tipos de Cuenta'
        ordering = ['act_id']

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True, verbose_name='ID')
    customer = models.ForeignKey(Cliente, models.CASCADE, verbose_name='cliente', related_name='cuentas')
    account_type = models.ForeignKey('TipoCuenta', models.DO_NOTHING,  db_column='account_type', verbose_name='Tipo de Cuenta', related_name='cuentas')
    balance = models.IntegerField(verbose_name='saldo')
    iban = models.TextField(verbose_name='Código Internacional de Cuentas Bancarias')

    def saldo_total(self):
        return self.balance / 100

    def saldo_con_formato(self):
        if self.balance >= 0:
            return 'AR$' + str(self.saldo_total()).replace('.',',')
        else:
            return '-AR$' + str(-self.saldo_total()).replace('.',',')

    def enviar_transferencia(self, otro, monto):
        if not isinstance(otro,Cuenta):
            raise TypeError(f"El parámtero 'otro' debe ser de tipo 'Cuenta' y es de tipo '{otro.__class__.__name__}'")
        if not isinstance(monto, int):
            raise TypeError(f"El parámtero 'monto' debe ser de tipo 'int' y es de tipo '{otro.__class__.__name__}'")
        if monto > self.balance:
            raise ValueError(f'Saldo insuficiente')

        self.balance -= monto
        self.save()
        Movimiento(movement_total=monto, movement_type='transf_env', customer=self.customer).save()
        otro.balance += monto
        otro.save()
        Movimiento(movement_total=monto, movement_type='transf_recib', customer=otro.customer).save()

    def recibir_prestamo(self,monto):
        self.balance += monto
        self.save()
        Movimiento(movement_total=monto, movement_type='prestamo', customer=self.customer).save()

    def __str__(self):
        return f"Cuenta nro."+str(self.account_id)

    class Meta:
        managed = True
        db_table = 'cuenta'
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['account_id']

class Movimiento(models.Model):
    movement_id = models.AutoField(primary_key=True, verbose_name='ID')
    movement_total = models.IntegerField(verbose_name='monto')
    movement_type = models.TextField(verbose_name='tipo',choices=[('transf_recib','Transferencia Recibida'),('transf_env','Transferencia Enviada'),('efectivo_ing','Ingreso Efectivo'),('efectivo_eg','Egreso Efectivo'),('prestamo','Préstamo Recibido')])
    movement_datetime = models.DateTimeField(verbose_name='fecha', auto_now_add=True)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='movimientos', verbose_name='cliente')

    def __str__(self):
        return "Transferecia nro. " + str(self.movement_id)

    def monto_total(self):
        return self.movement_total / 100

    def monto_con_formato(self):
        if self.movement_total >= 0:
            return '$' + str(self.monto_total()).replace('.',',')
        else:
            return '-$' + str(-self.monto_total()).replace('.',',')

    class Meta:
        managed = True
        db_table = 'movimientos'
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        ordering = ['movement_id']
