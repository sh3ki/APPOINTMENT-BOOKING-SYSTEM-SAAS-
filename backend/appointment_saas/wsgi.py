"""WSGI config for appointment_saas project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appointment_saas.settings")
application = get_wsgi_application()
