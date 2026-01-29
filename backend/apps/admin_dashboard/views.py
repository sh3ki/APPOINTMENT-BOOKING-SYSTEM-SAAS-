from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from apps.bookings.models import Booking
from apps.services.models import Service

User = get_user_model()


class AdminStatsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "users": User.objects.count(),
            "services": Service.objects.count(),
            "bookings": Booking.objects.count(),
            "revenue": 0,
        }
        return Response(data)


class BookingsExportCSVAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=bookings.csv"
        response.write("id,service,staff,customer,start_time,end_time,status\n")
        for booking in Booking.objects.all().order_by("-start_time"):
            response.write(
                f"{booking.id},{booking.service.name},{booking.staff.email},{booking.customer.email},{booking.start_time},{booking.end_time},{booking.status}\n"
            )
        return response
