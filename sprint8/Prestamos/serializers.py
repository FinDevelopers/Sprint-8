from rest_framework import serializers
from .models import Prestamo

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('loan_type', 'monto_total')
    
class PrestamoSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        exclude = ['loan_id']

class PrestamoSerializerDestroy(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['loan_id']