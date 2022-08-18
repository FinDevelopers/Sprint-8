from django.db import models
from Clientes.models import Cliente

# Create your models here.
class MarcaTarjeta(models.Model):
    cat_id = models.AutoField(primary_key=True, verbose_name='ID')
    cat_name = models.TextField(verbose_name='marca')

    def __str__(self):
        return self.cat_name

    class Meta:
        managed = True
        db_table = 'marca_tarjeta'
        verbose_name='Marca Tarjeta'
        verbose_name_plural = 'Marcas Tarjeta'
        ordering = ['cat_id']

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True, verbose_name='ID')
    brand = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING, db_column='card_brand', verbose_name='marca', related_name='tarjetas')
    card_number = models.TextField(unique=True, verbose_name='número', null=True)
    card_cvv = models.IntegerField(verbose_name='código valor de validación', null=True)
    card_from_date = models.DateTimeField(null=True, verbose_name='fecha de expedición')
    card_expiration_date = models.DateTimeField(null=True, verbose_name='fecha de expiración')
    card_type = models.TextField(verbose_name='tipo', choices=[('credit','Crédito'),('debit','Débito')])
    customer = models.ForeignKey(Cliente, models.CASCADE, verbose_name='cliente', related_name='tarjetas', null=True)

    def __str__(self):
        return 'Tarjeta nro. ' + self.card_number

    class Meta:
        managed = True
        db_table = 'tarjeta'
        verbose_name='Tarjeta'
        verbose_name_plural = 'Tarjetas'
        ordering = ['card_id']