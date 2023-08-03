from django.contrib import admin
from .models import Advertisements # импортирую свою модель
# py manage.py createsuperuser - создания аккаунта супер пользователя
# пароль не отображается
# http://127.0.0.1:8000/admin

# кастомный класс для модели
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display  = ['id', 'title','description','price','auction','created_at'] # какие поля должны отображатья в таблице



# регистрирую модели и 
admin.site.register(Advertisements, AdvertisementsAdmin)