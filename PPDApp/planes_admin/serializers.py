from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class MedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medida
        fields = '__all__'

class ReporteMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteMedida
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

        extra_kwargs = {
            "created_by": {"read_only": True},
            "updated_by": {"read_only": True},  # No requerirlos en el input del request
        }

    def validate_nombre(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("nombre")
        return value
    def validate_resolucion(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("resolucion")
        return value

    def create(self, validated_data):
        request = self.context.get("request")  # Obtener el usuario desde el contexto
        if request and request.user:
            validated_data["created_by"] = request.user
            validated_data["updated_by"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        print("Usuario Update: ",request.user.email)
        if request and request.user.email:
            validated_data["updated_by"] = request.user.email
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrganismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organismo
        fields = '__all__'

class PlanMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanMedida
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'