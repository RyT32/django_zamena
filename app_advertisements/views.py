from django.shortcuts import render # для отправки html по запросу пользователя

from django.http import HttpResponse

from .models import Cats

def db(request):
    Cats.objects.create(name = 'котик', age = 6, breed = 'обычный')
    cats = Cats.objects.get(id = 1)

    return HttpResponse(cats.age)

# функция представление
def index(request):
    return render(request, "index.html")

def top_sellers(request):
    return render(request, "top-sellers.html")



def top_sellers(request):
    return render(request, "top-sellers.html")


def test(request):
    return render(request, 'test.html')


def test2(request):
    return render(request, 'test2.html')