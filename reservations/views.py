from django.shortcuts import render, get_object_or_404
from workshops.models import Workshop


def create_reservation(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    context = {
        'workshop': workshop,
    }

    return render(request, 'reservations/reservations.html', context)
