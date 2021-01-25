from django.urls import path
from . import views

urlpatterns = [
    path('<int:workshop_id>', views.reservation, name='reservation'),
    path('book<int:workshop_id>', views.create_reservation, name='create_reservation'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]