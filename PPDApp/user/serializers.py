from rest_framework import serializers

class PermisosSerializer(serializers.Serializer):
    permisos = serializers.ListField(child=serializers.CharField())