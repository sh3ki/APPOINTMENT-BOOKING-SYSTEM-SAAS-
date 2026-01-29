"""ASGI config for appointment_saas project."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appointment_saas.settings")
application = get_asgi_application()
