from rest_framework import viewsets, permissions, status
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Booking, StaffAvailability, StaffTimeOff
from .serializers import BookingSerializer, StaffAvailabilitySerializer, StaffTimeOffSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by("-start_time")
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            queryset = Booking.objects.all()
        elif user.role == "staff":
            queryset = Booking.objects.filter(staff=user)
        else:
            queryset = Booking.objects.filter(customer=user)

        service_id = self.request.query_params.get("service")
        staff_id = self.request.query_params.get("staff")
        customer_id = self.request.query_params.get("customer")
        start_date = self.request.query_params.get("start")
        end_date = self.request.query_params.get("end")

        if service_id:
            queryset = queryset.filter(service_id=service_id)
        if staff_id:
            queryset = queryset.filter(staff_id=staff_id)
        if customer_id and user.role == "admin":
            queryset = queryset.filter(customer_id=customer_id)
        if start_date:
            queryset = queryset.filter(start_time__date__gte=start_date)
        if end_date:
            queryset = queryset.filter(start_time__date__lte=end_date)

        return queryset.order_by("-start_time")

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user, status=Booking.Status.CONFIRMED)

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        booking.cancel()
        return Response({"status": "canceled"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def reschedule(self, request, pk=None):
        booking = self.get_object()
        data = request.data.copy()
        if "start_time" in data and "end_time" not in data:
            new_start = parse_datetime(data["start_time"])
            if new_start is None:
                return Response({"detail": "Invalid start_time"}, status=status.HTTP_400_BAD_REQUEST)
            if timezone.is_naive(new_start):
                new_start = timezone.make_aware(new_start)
            data["end_time"] = (new_start + timezone.timedelta(minutes=booking.service.duration_minutes)).isoformat()
        serializer = self.get_serializer(booking, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class StaffAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = StaffAvailability.objects.all()
    serializer_class = StaffAvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]


class StaffTimeOffViewSet(viewsets.ModelViewSet):
    queryset = StaffTimeOff.objects.all()
    serializer_class = StaffTimeOffSerializer
    permission_classes = [permissions.IsAuthenticated]
