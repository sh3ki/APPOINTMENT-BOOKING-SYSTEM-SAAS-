from rest_framework import serializers


class AdminStatsSerializer(serializers.Serializer):
    users = serializers.IntegerField()
    services = serializers.IntegerField()
    bookings = serializers.IntegerField()
    revenue = serializers.DecimalField(max_digits=10, decimal_places=2)
