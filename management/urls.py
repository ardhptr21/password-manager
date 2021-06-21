from django.urls import path
from .views import (
    ManagementListView,
    ManagementCreateView
)

urlpatterns = [
    path('list/', ManagementListView.as_view(template_name="management/list.html"), name='list'),
    path('create/', ManagementCreateView.as_view(), name='create'),
    path('manage/', ManagementListView.as_view(template_name="management/manage.html"), name='manage'),
]
