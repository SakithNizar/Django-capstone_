from rest_framework import viewsets, permissions
from .models import Provider, Service
from .serializers import ProviderSerializer, ServiceSerializer
from .permissions import IsProviderOwner

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Provider, Service
from .serializers import ServiceSerializer
from rest_framework.permissions import IsAuthenticated

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def get_permissions(self):
        if self.action in ["update", "partial_update"]:
            permission_classes = [permissions.IsAuthenticated, IsProviderOwner]
        elif self.action == "destroy":
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [p() for p in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def create_service_for_provider(self, request, pk=None):
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return Response({"error": "Provider not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        data["provider"] = provider.id
        serializer = ServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)