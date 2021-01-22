from django.shortcuts import render
from .models import UserProfile


def profile(request):
    user = UserProfile.objects.all()
    context = {
        'user': user,
    }
    return render(request, 'profiles/profile.html', context)
