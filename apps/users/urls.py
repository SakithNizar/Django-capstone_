from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.users.urls')),  # <-- include users app URLs
    path('api/providers/', include('apps.providers.urls')),  # optional if you have providers
]