from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from workshops.models import Workshop
from .forms import OrderForm
from django.conf import settings
import stripe


def create_reservation(request, workshop_id):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    workshop = get_object_or_404(Workshop, pk=workshop_id)
    order_form = OrderForm()
    template = 'reservations/reservations.html'
    price = workshop.price
    stripe_total = round(price * 100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    context = {
        'workshop': workshop,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
