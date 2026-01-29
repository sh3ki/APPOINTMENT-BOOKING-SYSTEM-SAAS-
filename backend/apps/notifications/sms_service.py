import os
from twilio.rest import Client


def send_sms(to_number: str, body: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID", "")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN", "")
    from_number = os.getenv("TWILIO_FROM_NUMBER", "")
    if not account_sid or not auth_token or not from_number:
        raise ValueError("Twilio credentials not configured")
    client = Client(account_sid, auth_token)
    return client.messages.create(to=to_number, from_=from_number, body=body)
