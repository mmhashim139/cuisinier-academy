from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<int:workshop_id>', views.reservation, name='reservation'),
    path('book<int:workshop_id>', views.create_reservation, name='create_reservation'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]