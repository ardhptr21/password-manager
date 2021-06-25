from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def logoutView(request):
    logout(request)
    return redirect('auth:login')


class AuthLoginView(LoginView):
    template_name = 'auth/login.html'


def register(request):
    return render(request, template_name='auth/register.html')
