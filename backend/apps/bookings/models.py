from django.conf import settings
from django.db import models
from django.utils import timezone
from apps.services.models import Service


class StaffAvailability(models.Model):
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="availability")
    weekday = models.PositiveSmallIntegerField()  # 0=Mon ... 6=Sun
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("staff", "weekday", "start_time", "end_time")


class StaffTimeOff(models.Model):
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="time_off")
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    reason = models.CharField(max_length=255, blank=True)


class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        CANCELED = "canceled", "Canceled"
        COMPLETED = "completed", "Completed"

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="bookings")
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="staff_bookings")
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer_bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    notes = models.TextField(blank=True)
    canceled_at = models.DateTimeField(null=True, blank=True)
    cancellation_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def cancel(self, fee=None):
        self.status = self.Status.CANCELED
        self.canceled_at = timezone.now()
        if fee is not None:
            self.cancellation_fee = fee
        self.save()

    def __str__(self) -> str:
        return f"{self.service.name} - {self.customer_id}"
