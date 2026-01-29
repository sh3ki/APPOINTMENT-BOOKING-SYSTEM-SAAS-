import pytest
from .models import Service


@pytest.mark.django_db
def test_create_service():
    service = Service.objects.create(name="Consultation", price=100, duration_minutes=60)
    assert service.name == "Consultation"
