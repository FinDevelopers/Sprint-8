from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('customer_name', 'customer_surname', 'customer_dni', 'dob', 'branch', 'client_type', 'cuentas')
        read_only_fields = ['account_id', 'user']