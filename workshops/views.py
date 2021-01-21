from django.shortcuts import render, get_object_or_404
from .models import Workshop
from experts.models import Expert


# Create your views here.
def workshops(request):
    workshops = Workshop.objects.all()
    for workshop in workshops:
        expert = Expert.objects.filter(name=workshop.expert)

    context = {
        'workshops': workshops,
        'expert': expert,
    }

    return render(request, 'workshops/workshops.html', context)


def workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    expert = Expert.objects.filter(name=workshop.expert)

    context = {
        'workshop': workshop,
        'expert' : expert,
    }

    return render(request, 'workshops/workshop.html', context)
