from django.urls import path
from .views import (
    ManagementListView,
    ManagementCreateView,
    ManagementUpdateView,
    ManagementDeleteView
)

urlpatterns = [
    path('update/<int:pk>/', ManagementUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ManagementDeleteView.as_view(), name='delete'),
    path('list/', ManagementListView.as_view(template_name="management/list.html"), name='list'),
    path('create/', ManagementCreateView.as_view(), name='create'),
    path('manage/', ManagementListView.as_view(template_name="management/manage.html"), name='manage'),
]
