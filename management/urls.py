from django.urls import path
from django.views.generic.base import TemplateView
from .views import (
    ManagementListView,
)

urlpatterns = [
    path('list/', ManagementListView.as_view(), name='list'),
    path('create/', TemplateView.as_view(template_name="management/create.html"), name='create')
]
