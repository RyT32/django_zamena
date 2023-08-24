# маршрутизатор приложения
from django.urls import path

from .views import profile



urlpatterns = [
    path('profile/', profile, name='profile'), # http://127.0.0.1:8000/auth/profile/
]


 