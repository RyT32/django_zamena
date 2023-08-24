from django.shortcuts import render,redirect # redirect - переадресация 
from django.urls import reverse # получение ссылки полной по название в urls
from django.core.handlers.wsgi import WSGIRequest


def profile(request):
    return render(request,'profile.html')

def logout_view(request):
    return render(request,'profile.html')

def sign_in(request):
    return render(request,'register.html')

def login_view(request: WSGIRequest):
    if request.method == 'POST':
        pass

    elif request.method == 'GET': # просто заходит на страницу login
        if request.user.is_authenticated: # если пользователь авторизован,то
            # ему не нужна страница входа
            return redirect(reverse('profile'))# перенаправляем на страницу профиля
        else:# иначе
            return render(request,'login.html')