from django.db import models
from django.utils import timezone
from apps.providers.models import Service

class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="bookings")
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    booking_date = models.DateField()
    number_of_guests = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.booking_date < timezone.now().date():
            raise ValueError("Booking date must be in the future.")
        if not self.service.is_active:
            raise ValueError("Cannot book an inactive service.")
        self.total_price = self.number_of_guests * self.service.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} - {self.service.title}"