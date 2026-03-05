from rest_framework.permissions import BasePermission

class IsBookingOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer_email == request.user.email