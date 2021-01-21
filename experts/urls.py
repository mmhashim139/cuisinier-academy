from django.urls import path

from . import views

urlpatterns = [
    path('', views.experts, name='experts'),
    path('<int:expert_id>', views.expert, name='expert'),
]