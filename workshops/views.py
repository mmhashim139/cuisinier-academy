from django.shortcuts import render


# Create your views here.
def workshops(request):
    return render(request, 'workshops/workshops.html')


def workshop(request):
    return render(request, 'workshops/workshop.html')
