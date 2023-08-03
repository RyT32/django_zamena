from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
# Create your models here.
# тестовый класс
class Cats(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)



# главный


# заголовок - описание - цена - дата создания - дата обновления - тогр


class Advertisements(models.Model):
    title = models.CharField('заголовок',max_length=100)
    descriptoin = models.TextField('описание')
    price = models.DecimalField('цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text='Возможен торг или нет',default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    





    # представление в виде строки 
    def __str__(self) -> str:
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

    # настройки для таблицы
    class Meta:
        db_table = 'advertisements' # переименовали таблицу 



#         from app_advertisements.models import Advertisements                                
#         adv1 = Advertisements (title = 'Молоко', descriptoin = 'Свежее молоко', price = 100, auction = True)   # создаю запись                           
#         adv1.save()           #сохраняю                      
#                                       
# from django.db import connection                              
# connection.queries     # получаю все запросы к sql                            
#                                       
                                    















