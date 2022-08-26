from rest_framework import serializers
from .models import Cliente, Sucursal, Direccion

class ClienteSerializer(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()
    client_type = serializers.StringRelatedField()
    class Meta:
        model = Cliente
        fields = ('customer_name', 'customer_surname', 'customer_dni', 'dob', 'branch', 'client_type', 'cuentas_asociadas')
        read_only_fields = ['account_id', 'user']

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class DireccionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        exclude = ('address_customer','address_employee','address_branch')

