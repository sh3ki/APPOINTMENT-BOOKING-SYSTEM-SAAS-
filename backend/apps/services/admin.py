from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "duration_minutes")
    search_fields = ("name", "category")
