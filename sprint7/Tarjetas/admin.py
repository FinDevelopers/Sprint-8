from django.contrib import admin
from .models import Tarjeta, MarcaTarjeta

# Register your models here.
class MarcaTarjetaAdmin(admin.ModelAdmin):
    list_display=['cat_id','cat_name']
    list_display_links = ['cat_name']
admin.site.register(MarcaTarjeta,MarcaTarjetaAdmin)


class TarjetaAdmin(admin.ModelAdmin):
    list_display = ['card_id','card_number','customer','brand','card_type']
    list_display_links = ['card_number']
admin.site.register(Tarjeta,TarjetaAdmin)
