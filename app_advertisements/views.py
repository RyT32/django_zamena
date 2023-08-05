from django.shortcuts import render # для отправки html по запросу пользователя

from django.http import HttpResponse
from .models import Advertisements # импортировал модель обьявления 


# функция представление
def index(request):
    advertisiments =  Advertisements.objects.all() # все записи
    context = {'advertisiments': advertisiments}
    return render(request, "index.html", context)

def top_sellers(request):
    return render(request, "top-sellers.html")



def top_sellers(request):
    return render(request, "top-sellers.html")


def test(request):
    return render(request, 'test.html')


def test2(request):
    return render(request, 'test2.html')