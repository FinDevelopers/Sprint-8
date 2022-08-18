from rest_framework import serializers
from .models import Cuenta

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('account_id', 'customer', 'account_type', 'balance', 'iban')
        read_only_fields = ['account_id']
