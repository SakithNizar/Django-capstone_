from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    service_title = serializers.CharField(source="service.title", read_only=True)
    provider_name = serializers.CharField(source="service.provider.name", read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ["total_price", "status", "created_at"]