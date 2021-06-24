from django.shortcuts import render
from django.contrib.auth.views import LoginView


def login(request):
    return render(request, template_name='auth/login.html')


class AuthLoginView(LoginView):
    template_name = 'auth/login.html'


def register(request):
    return render(request, template_name='auth/register.html')
