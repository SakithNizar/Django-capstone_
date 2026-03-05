from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsBookingOwner

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsBookingOwner]

    def get_queryset(self):
        return Booking.objects.filter(customer_email=self.request.user.email)

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        if booking.status != "pending":
            return Response({"error": "Only pending bookings can be cancelled"}, status=status.HTTP_400_BAD_REQUEST)
        booking.status = "cancelled"
        booking.save()
        return Response({"status": "cancelled"})