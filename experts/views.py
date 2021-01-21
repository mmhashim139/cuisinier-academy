from django.shortcuts import render
from .models import Expert


def experts(request):
    experts = Expert.objects.all()
    context = {
        'experts': experts,
    }

    return render(request, 'experts/experts.html', context)
