from django.shortcuts import render
from django.views.generic import ListView
from .models import Account


class ManagementListView(ListView):
    model = Account
    template_name = 'management/list.html'
    ordering = ('id',)
    context_object_name = 'accounts'
