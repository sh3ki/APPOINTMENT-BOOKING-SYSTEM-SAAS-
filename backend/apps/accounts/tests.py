import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username="user1", email="user1@example.com", password="pass1234")
    assert user.email == "user1@example.com"
    assert user.check_password("pass1234")
