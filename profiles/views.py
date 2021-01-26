from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def profile(request):
    user = get_object_or_404(UserProfile, user=request.user)
    context = {
        'user': user,
    }
    return render(request, 'profiles/profile.html', context)
