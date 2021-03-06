from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('workshops/', include('workshops.urls')),
    path('experts/', include('experts.urls')),
    path('profiles/', include('profiles.urls')),
    path('reservations/', include('reservations.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
