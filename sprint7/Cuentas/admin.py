from django.contrib import admin
from .models import TipoCuenta, Cuenta, Movimiento

# Register your models here.
class TipoCuentaAdmin(admin.ModelAdmin):
    list_display = ['act_id', 'act_name']
    list_display_links = ['act_name']
admin.site.register(TipoCuenta, TipoCuentaAdmin)


class CuentaAdmin(admin.ModelAdmin):
    list_display = ['account_id', 'iban', 'customer', 'account_type','saldo_con_formato']
    list_display_links = ['iban']
admin.site.register(Cuenta, CuentaAdmin)


class MovimientoAdmin(admin.ModelAdmin):
    list_display = ['movement_id', 'customer', 'movement_type', 'monto_con_formato'] 
    list_display_links = ['customer']
    readonly_fields= ['movement_datetime']
    
admin.site.register(Movimiento, MovimientoAdmin)