from django.urls import path
from .views import RegisterAPIView, ProfileAPIView, StaffListAPIView, EmailTokenObtainPairView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("me/", ProfileAPIView.as_view(), name="profile"),
    path("staff/", StaffListAPIView.as_view(), name="staff-list"),
    path("token/", EmailTokenObtainPairView.as_view(), name="email-token"),
]
