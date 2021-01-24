from django.shortcuts import render, get_object_or_404, redirect
from workshops.models import Workshop


def create_reservation(request, workshop_id):
    # if user authinticated , else login / crete an acount
    if request.user.is_authenticated:
        workshop = get_object_or_404(Workshop, pk=workshop_id)
        user = request.user
        context = {
            'workshop': workshop,
            'user': user,
            }
        return render(request, 'reservations/reservations.html', context)

    else:
        # login and then redirect to the orfer page ???
        template = "account/login.html"
        return render(request, template)
