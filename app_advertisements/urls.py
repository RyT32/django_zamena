# маршрутизатор приложения
from django.urls import path

from .views import index, top_sellers , db



urlpatterns = [
    path('', index, name='index'),
    path('db', db, name='db'),

    path('top_sellers', top_sellers, name='top_sellers'),


]


 