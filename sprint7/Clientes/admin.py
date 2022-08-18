from django.contrib import admin
from .models import Cliente, TipoCliente, Sucursal, Empleado, Direccion

# Register your models here.
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['branch_id','branch_name'] 
    list_display_links = ['branch_name']
admin.site.register(Sucursal, SucursalAdmin)

class TipoClienteAdmin(admin.ModelAdmin):
    list_display= ['clt_id','clt_name']
    list_display_links = ['clt_name']
admin.site.register(TipoCliente, TipoClienteAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display= ['customer_id','nombre_completo','client_type','user']
    list_display_links= ['nombre_completo']
    list_filter= ['client_type']
admin.site.register(Cliente, ClienteAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display= ['employee_id','nombre_completo','employee_hire_date', 'branch']
    list_display_links = ['nombre_completo']
admin.site.register(Empleado, EmpleadoAdmin)

class DireccionAdmin(admin.ModelAdmin):
    list_display= ['address_id','calle_y_ciudad','address_customer', 'address_employee', 'address_branch']
    list_display_links = ['calle_y_ciudad']
    empty_value_display = ''
admin.site.register(Direccion, DireccionAdmin)

