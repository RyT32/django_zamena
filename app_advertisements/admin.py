from django.contrib import admin
from .models import Advertisements

# импортирую классы для подсказок
from django.db.models.query import QuerySet

# Register your models here.
# py manage.py createsuperuser - создание аккаунта админа


class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id','title','descriptoin','price','auction', 'created_date', 'update_date']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false','make_auction_as_true'] # указываю функции
    fieldsets = (  # при добавлении записей указываем кастомизацию
        ( # 1 блок
            'Общее', # название блока
            {
                "fields":('title','descriptoin')
            }
        ),
        (   # 2 блок
            'Финансы', # название блока
            {
                "fields":('price','auction'),
                'classes':['collapse'] # для скрытия 
            }
        )
    )




    #создаю функции
    @admin.action(description='Убрать возможность торга')# менять у записей торг на False
    def make_auction_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')# менять у записей торг на False
    def make_auction_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True)
        

    






# указал модель и админ класс(для кастомизации)
admin.site.register(Advertisements, AdvertisementsAdmin)