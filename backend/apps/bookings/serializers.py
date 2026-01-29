from django.utils import timezone
from rest_framework import serializers
from .models import Booking, StaffAvailability, StaffTimeOff


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ["id", "customer", "status", "created_at", "canceled_at"]

    def validate(self, attrs):
        staff = attrs.get("staff") or getattr(self.instance, "staff", None)
        service = attrs.get("service") or getattr(self.instance, "service", None)
        start_time = attrs.get("start_time") or getattr(self.instance, "start_time", None)
        end_time = attrs.get("end_time") or getattr(self.instance, "end_time", None)
        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError("End time must be after start time")
        if start_time and start_time < timezone.now():
            raise serializers.ValidationError("Start time must be in the future")
        if start_time and service and not end_time:
            end_time = start_time + timezone.timedelta(minutes=service.duration_minutes)
            attrs["end_time"] = end_time
        if staff and start_time and end_time:
            overlap = Booking.objects.filter(
                staff=staff,
                status__in=[Booking.Status.PENDING, Booking.Status.CONFIRMED],
                start_time__lt=end_time,
                end_time__gt=start_time,
            ).exists()
            if overlap:
                raise serializers.ValidationError("Staff already booked for that time")
            weekday = start_time.weekday()
            has_availability = StaffAvailability.objects.filter(
                staff=staff,
                weekday=weekday,
                is_available=True,
                start_time__lte=start_time.time(),
                end_time__gte=end_time.time(),
            ).exists()
            if not has_availability:
                raise serializers.ValidationError("Staff is not available for that time")
            time_off = StaffTimeOff.objects.filter(
                staff=staff,
                date=start_time.date(),
            )
            if time_off.exists():
                raise serializers.ValidationError("Staff is unavailable due to time off")
        return attrs


class StaffAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAvailability
        fields = "__all__"


class StaffTimeOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffTimeOff
        fields = "__all__"
