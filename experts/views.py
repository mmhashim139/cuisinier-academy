from django.shortcuts import render, get_object_or_404
from .models import Expert
from workshops.models import Workshop


def experts(request):
    experts = Expert.objects.all()
    workshops = Workshop.objects.all()

    context = {
        'experts': experts,
        'workshops': workshops,
    }

    return render(request, 'experts/experts.html', context)


def expert(request, expert_id):
    expert = get_object_or_404(Expert, pk=expert_id)
    workshop = list(Workshop.objects.filter(expert=expert))

    context = {
        'expert': expert,
        'workshop': workshop
    }

    return render(request, 'experts/expert.html', context)
