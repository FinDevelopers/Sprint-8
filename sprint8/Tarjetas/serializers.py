from rest_framework import serializers
from .models import Tarjeta

class TarjetaSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    class Meta:
        model = Tarjeta
        fields = '__all__'

