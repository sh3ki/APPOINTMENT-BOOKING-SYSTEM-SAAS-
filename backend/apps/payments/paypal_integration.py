import os
import paypalrestsdk

paypalrestsdk.configure(
    {
        "mode": os.getenv("PAYPAL_MODE", "sandbox"),
        "client_id": os.getenv("PAYPAL_CLIENT_ID", ""),
        "client_secret": os.getenv("PAYPAL_CLIENT_SECRET", ""),
    }
)


def create_payment(amount: str, currency: str = "USD"):
    payment = paypalrestsdk.Payment(
        {
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "transactions": [{"amount": {"total": amount, "currency": currency}}],
            "redirect_urls": {"return_url": "", "cancel_url": ""},
        }
    )
    if not payment.create():
        raise RuntimeError(payment.error)
    return payment
