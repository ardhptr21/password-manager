from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Account
from .forms import ManagementCreateForm


class ManagementListView(ListView):
    model = Account
    template_name = 'management/list.html'
    ordering = ('-id',)
    context_object_name = 'accounts'


class ManagementCreateView(CreateView):
    form_class = ManagementCreateForm
    template_name = 'management/create.html'
