import pytest
from django.utils import timezone
from django.contrib.auth import get_user_model
from apps.services.models import Service
from .models import Booking

User = get_user_model()


@pytest.mark.django_db
def test_double_booking_blocked():
    staff = User.objects.create_user(username="staff", email="staff@example.com", password="pass1234")
    customer = User.objects.create_user(username="customer", email="cust@example.com", password="pass1234")
    service = Service.objects.create(name="Consult", price=100, duration_minutes=60)
    start = timezone.now() + timezone.timedelta(days=1)
    end = start + timezone.timedelta(hours=1)
    Booking.objects.create(service=service, staff=staff, customer=customer, start_time=start, end_time=end)
    overlap = Booking.objects.filter(
        staff=staff,
        start_time__lt=end,
        end_time__gt=start,
        status__in=[Booking.Status.PENDING, Booking.Status.CONFIRMED],
    ).exists()
    assert overlap is True
