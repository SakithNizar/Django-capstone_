from django.db import models
from django.contrib.auth import get_user_model

class Provider(models.Model):
    BUSINESS_CHOICES = [
        ("hotel", "Hotel"),
        ("restaurant", "Restaurant"),
        ("tour_operator", "Tour Operator"),
        ("transport", "Transport"),
        ("experience", "Experience"),
    ]

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    business_type = models.CharField(max_length=50, choices=BUSINESS_CHOICES)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_hours = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title