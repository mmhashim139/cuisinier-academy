from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from workshops.models import Workshop
from .forms import OrderForm


def create_reservation(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    order_form = OrderForm()
    template = 'reservations/reservations.html'
    context = {
        'workshop': workshop,
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I8HbBFN2cRN53XosVSXRQvzc1gOWhDyGzIn8YGNwGtx78gC81X7SW38cMy4P1poeVIcIVXUxEEw9CorOv0bZIhq00vKwt6zkH',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
