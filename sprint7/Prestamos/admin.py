from django.contrib import admin
from .models import Prestamo
# Register your models here.

class PrestamoAdmin(admin.ModelAdmin):
    list_display=['loan_id','customer','tipo_cliente','loan_type','monto_con_formato']
    list_display_links = ['loan_id']
    list_filter= ['loan_type']
admin.site.register(Prestamo,PrestamoAdmin)