from rest_framework import serializers
from .models import Provider, Service

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"
        read_only_fields = ["owner", "is_verified", "created_at"]


class ServiceSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source="provider.name", read_only=True)

    class Meta:
        model = Service
        fields = "__all__"
        read_only_fields = ["provider", "created_at"]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive.")
        return value