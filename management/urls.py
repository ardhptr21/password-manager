from django.urls import path
from django.views.generic.base import TemplateView
urlpatterns = [
    path('list/', TemplateView.as_view(template_name="management/list.html"), name='list'),
    path('create/', TemplateView.as_view(template_name="management/create.html"), name='create')
]
