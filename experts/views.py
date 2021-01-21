from django.shortcuts import render
from .models import Expert
from workshops.models import Workshop


def experts(request):
    experts = Expert.objects.all()
    for expert in experts:
        workshop = list(Workshop.objects.filter(expert=expert))

    context = {
        'experts': experts,
        'workshop': workshop
    }

    return render(request, 'experts/experts.html', context)
