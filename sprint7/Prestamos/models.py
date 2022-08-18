from django.db import models
from Clientes.models import Cliente

# Create your models here.
class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True, verbose_name='ID')
    loan_type = models.TextField(choices=[('HIPOTECARIO','Hipotecario'),('PRENDARIO','Prendario'),('PERSONAL','Personal')], verbose_name='tipo de Préstamo')
    loan_date = models.TextField(verbose_name='fecha de vencimiento')
    loan_total = models.IntegerField(verbose_name='monto')
    customer = models.ForeignKey(Cliente,  on_delete=models.CASCADE, null=True, blank=True, related_name='prestamos', verbose_name='cliente') 

    def monto_total(self):
        return self.loan_total / 100

    def monto_con_formato(self):
        return '$' + str(self.monto_total()).replace('.',',')

    def tipo_cliente(self):
        return self.customer.client_type

    class Meta:
        managed = True
        db_table = 'prestamo'
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
        ordering = ['loan_id']