from django.urls import path
from .views import AuthLoginView, logoutView

urlpatterns = [
    path('login/', AuthLoginView.as_view(), name='login'),
    path('logout', logoutView, name="logout")
]
