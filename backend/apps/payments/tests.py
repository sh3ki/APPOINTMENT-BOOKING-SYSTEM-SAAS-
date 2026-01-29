import pytest
from django.utils import timezone
from django.contrib.auth import get_user_model
from apps.services.models import Service
from apps.bookings.models import Booking
from .models import PaymentTransaction

User = get_user_model()


@pytest.mark.django_db
def test_payment_create():
    staff = User.objects.create_user(username="staff2", email="staff2@example.com", password="pass1234")
    customer = User.objects.create_user(username="cust2", email="cust2@example.com", password="pass1234")
    service = Service.objects.create(name="Therapy", price=50, duration_minutes=60)
    start = timezone.now() + timezone.timedelta(days=1)
    end = start + timezone.timedelta(hours=1)
    booking = Booking.objects.create(service=service, staff=staff, customer=customer, start_time=start, end_time=end)
    payment = PaymentTransaction.objects.create(
        booking=booking,
        provider=PaymentTransaction.Provider.STRIPE,
        amount=10,
        currency="USD",
        created_by=customer,
    )
    assert payment.provider == "stripe"
