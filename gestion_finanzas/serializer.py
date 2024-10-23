from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields='__all__'

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields='__all__'

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields='__all__'

class ObjetivoAhorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetivoAhorro
        fields='__all__'

class PresupuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presupuesto
        fields='__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields='__all__'