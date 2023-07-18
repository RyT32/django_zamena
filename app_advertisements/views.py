from django.shortcuts import render # для отправки html по запросу пользователя

from django.http import HttpResponse

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