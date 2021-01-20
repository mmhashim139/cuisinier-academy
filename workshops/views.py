from django.shortcuts import render, get_object_or_404
from .models import Workshop


# Create your views here.
def workshops(request):
    workshops = Workshop.objects.all()

    context = {
        'workshops': workshops,
    }

    return render(request, 'workshops/workshops.html', context)


def workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)

    context = {
        'workshop': workshop
    }

    return render(request, 'workshops/workshop.html', context)
