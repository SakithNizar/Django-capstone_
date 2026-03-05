from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Booking
from apps.providers.models import Service
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def book_service(self, request, pk=None):
        try:
            service = Service.objects.get(pk=pk, is_active=True)
        except Service.DoesNotExist:
            return Response({"error": "Service not found or inactive"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        data["service"] = service.id
        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)