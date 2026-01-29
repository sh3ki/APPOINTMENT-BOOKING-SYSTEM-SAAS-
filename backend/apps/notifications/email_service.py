from django.core.mail import send_mail
from django.conf import settings


def send_booking_email(to_email: str, subject: str, message: str):
    return send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])
