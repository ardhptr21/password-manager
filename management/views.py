from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Account
from .forms import ManagementCreateForm


class ManagementListView(ListView):
    model = Account
    ordering = ('-id',)
    context_object_name = 'accounts'


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
