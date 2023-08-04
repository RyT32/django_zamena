from django.contrib import admin
from .models import Advertisements # импортирую свою модель
# класс обьекта модели для подсказки
from django.db.models.query import QuerySet

# py manage.py createsuperuser - создания аккаунта супер пользователя
# пароль не отображается
# http://127.0.0.1:8000/admin



# класс для кастомизации модели в админке
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','auction','created_at'] # столбцы для отображения в таблице

# подключение модели в админку и кастомной модели
admin.site.register(Advertisements, AdvertisementsAdmin)













# def add_list(some_list : list):
#     some_list.append()

# add_list()