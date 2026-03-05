# config/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.providers.views import ProviderViewSet, ServiceViewSet
from apps.bookings.views import BookingViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.users.views import RegisterView

router = DefaultRouter()

router.register("providers", ProviderViewSet, basename="provider")
router.register("services", ServiceViewSet, basename="service")
router.register("bookings", BookingViewSet, basename="booking")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/register/", RegisterView.as_view(), name="auth-register"),
    

    # JWT Auth Endpoints
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]