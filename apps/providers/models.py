from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name