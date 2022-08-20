from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True, null=False, verbose_name='ID')
    branch_number = models.IntegerField(verbose_name='número')
    branch_name = models.TextField(verbose_name='nombre')
    branch_address_id = models.IntegerField(verbose_name='ID Dirección')

    def __str__(self):
        return f"{self.branch_name}"

    class Meta:
        managed = False
        db_table = 'sucursal'
        verbose_name = 'Sucursal'
        verbose_name_plural ='Sucursales'
        ordering = ['branch_id']


class TipoCliente(models.Model):
    clt_id = models.AutoField(primary_key=True, null=False, verbose_name='id')
    clt_name = models.TextField(blank=True, null=True, verbose_name='nombre')

    def __str__(self):
        return f"{self.clt_name}"

    class Meta:
        managed = False
        db_table = 'tipo_cliente'
        verbose_name = 'Tipo Cliente'
        verbose_name_plural ='Tipos de Cliente'
        ordering = ['clt_id']


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True,null=False, verbose_name='ID')
    customer_name = models.TextField(verbose_name='nombre')
    customer_surname = models.TextField(verbose_name='apellido')  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI', verbose_name='DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True, verbose_name='fecha de nacimiento')
    branch = models.ForeignKey(Sucursal,  on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Sucursal', related_name='clientes')
    client_type =  models.ForeignKey(TipoCliente, on_delete=models.DO_NOTHING, verbose_name='Tipo cliente', related_name='clientes')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Usuario', related_name='cliente')

    def nombre_completo(self):
        return f"{self.customer_name} {self.customer_surname}"

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        managed = True
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['customer_id']


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True, verbose_name='ID')
    employee_name = models.TextField(verbose_name='nombre')
    employee_surname = models.TextField(verbose_name='apellido')
    employee_hire_date = models.TextField(verbose_name='fecha de contratación')
    employee_dni = models.TextField(db_column='employee_DNI', verbose_name='DNI')  # Field name made lowercase.
    #Se eliminaron los empleados con id 0 para agregar la fK
    branch = models.ForeignKey(Sucursal, on_delete=models.CASCADE, verbose_name='sucursal', related_name='empleados')

    def nombre_completo(self):
        return f"{self.employee_name} {self.employee_surname}"

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        managed = True
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['employee_id']

    

class Direccion(models.Model):
    address_id = models.AutoField(primary_key=True, verbose_name='ID')
    address_street = models.TextField(verbose_name='calle')
    address_number = models.TextField(verbose_name='numero')
    address_city = models.TextField(verbose_name='ciudad')
    address_province = models.TextField(verbose_name='provincia')
    address_country = models.TextField(verbose_name='país')
    address_customer = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='cliente', related_name = 'direcciones')
    address_employee = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='empleado', related_name = 'direcciones')
    address_branch = models.OneToOneField(Sucursal, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='sucursal', related_name = 'direccion')

    def calle_y_ciudad(self):
        return f"{self.address_street} {self.address_number}, {self.address_city}"

    def __str__(self):
        return self.calle_y_ciudad()

    class Meta:
        managed = True
        db_table = 'direccion'
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'
        ordering = ['address_id']



