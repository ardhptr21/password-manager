from django.http import request
from django.utils.datastructures import MultiValueDict, MultiValueDictKeyError
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Account
from .forms import ManagementCreateForm


class ManagementListView(ListView):
    model = Account
    ordering = ('-id',)
    context_object_name = 'accounts'

    def get_queryset(self):
        try:
            search = self.request.GET['search']
            return self.model.objects.filter(site_name__icontains=search)
        except MultiValueDictKeyError:
            return super().get_queryset()


class ManagementCreateView(CreateView):
    form_class = ManagementCreateForm
    template_name = 'management/create.html'


class ManagementUpdateView(UpdateView):
    model = Account
    fields = '__all__'
    template_name = 'management/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'img_url': self.get_object().image_site.url})
        return context


class ManagementDeleteView(DeleteView):
    model = Account
    template_name = 'management/delete_confirm.html'
    success_url = reverse_lazy('management:manage')
