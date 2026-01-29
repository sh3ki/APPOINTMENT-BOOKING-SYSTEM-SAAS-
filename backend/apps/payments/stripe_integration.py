import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "")


def create_payment_intent(amount_cents: int, currency: str = "usd"):
    if not stripe.api_key:
        raise ValueError("Stripe key not configured")
    return stripe.PaymentIntent.create(amount=amount_cents, currency=currency)
