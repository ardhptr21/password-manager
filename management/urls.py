from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    ManagementListView,
    ManagementCreateView,
    ManagementUpdateView,
    ManagementDeleteView
)

urlpatterns = [
    path('update/<int:pk>/',
         login_required(ManagementUpdateView.as_view()), name='update'),
    path('delete/<int:pk>/',
         login_required(ManagementDeleteView.as_view()), name='delete'),
    path('list/',
         login_required(ManagementListView.as_view(template_name="management/list.html")), name='list'),
    path('create/',
         login_required(ManagementCreateView.as_view()), name='create'),
    path('manage/',
         login_required(ManagementListView.as_view(template_name="management/manage.html")), name='manage'),
]
