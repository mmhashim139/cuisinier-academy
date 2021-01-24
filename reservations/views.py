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
    }

    return render(request, template, context)
