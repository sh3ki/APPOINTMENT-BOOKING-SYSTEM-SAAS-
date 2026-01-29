from django.contrib import admin
from .models import Booking, StaffAvailability, StaffTimeOff


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "service", "staff", "customer", "start_time", "status")
    list_filter = ("status",)
    search_fields = ("service__name", "customer__email", "staff__email")


admin.site.register(StaffAvailability)
admin.site.register(StaffTimeOff)
