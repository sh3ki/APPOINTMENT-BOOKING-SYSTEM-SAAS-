from django.urls import path
from .views import AdminStatsAPIView, BookingsExportCSVAPIView

urlpatterns = [
    path("stats/", AdminStatsAPIView.as_view(), name="admin-stats"),
    path("bookings-export/", BookingsExportCSVAPIView.as_view(), name="bookings-export"),
]
