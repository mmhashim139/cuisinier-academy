from django.urls import path
from . import views

urlpatterns = [
    path('book<int:workshop_id>', views.create_reservation, name='create_reservation'),
]