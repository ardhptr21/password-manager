from django.urls import path
from .views import (
    ManagementListView,
    ManagementCreateView
)

urlpatterns = [
    path('list/', ManagementListView.as_view(), name='list'),
    path('create/', ManagementCreateView.as_view(), name='create')
]
