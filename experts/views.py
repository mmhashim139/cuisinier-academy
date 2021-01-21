from django.shortcuts import render


def experts(request):
    return render(request, 'experts/experts.html')

