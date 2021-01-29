from django.shortcuts import render
from experts.models import Expert
from workshops.models import Workshop
# Create your views here.


def index(request):
    experts = Expert.objects.all()[:3]
    workshops = Workshop.objects.all()[:4]
    context = {
        'experts': experts,
        'workshops': workshops,
    }

    return render(request, 'home/index.html', context)
