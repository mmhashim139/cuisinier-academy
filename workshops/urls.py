from django.urls import path

from . import views

urlpatterns = [
    path('', views.workshops, name='workshops'),
    path('workshop', views.workshop, name='workshop'),
]
