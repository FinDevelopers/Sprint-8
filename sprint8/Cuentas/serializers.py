from rest_framework import serializers
from .models import Cuenta

class CuentaSerializer(serializers.ModelSerializer):
    account_type = serializers.StringRelatedField()
    class Meta:
        model = Cuenta
        fields = ('account_type', 'saldo_total')

