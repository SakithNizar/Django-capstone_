from rest_framework import viewsets, permissions
from .models import Provider, Service
from .serializers import ProviderSerializer, ServiceSerializer
from .permissions import IsProviderOwner

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
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        provider_id = self.kwargs.get("provider_pk")
        serializer.save(provider_id=provider_id)