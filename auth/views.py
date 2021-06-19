from django.shortcuts import render


def login(request):
    return render(request, template_name='auth/login.html')


def register(request):
    return render(request, template_name='auth/register.html')
