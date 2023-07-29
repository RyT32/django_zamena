from django.contrib import admin
from .models import Advertisements
# Register your models here.
# py manage.py createsuperuser - создание аккаунта админа

# указал модель и админ класс(для кастомизации)
admin.site.register(Advertisements)