from django.db import models
from django.conf import settings


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(default=30)
    category = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    addons = models.JSONField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="created_services", on_delete=models.SET_NULL, null=True
    )
    staff = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="services", blank=True)

    def __str__(self) -> str:
        return self.name
