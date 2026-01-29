from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, StaffAvailabilityViewSet, StaffTimeOffViewSet

router = DefaultRouter()
router.register(r"", BookingViewSet, basename="booking")
router.register(r"availability", StaffAvailabilityViewSet, basename="availability")
router.register(r"time-off", StaffTimeOffViewSet, basename="time-off")

urlpatterns = router.urls
