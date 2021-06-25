from django.urls import path
from .views import register, AuthLoginView, logoutView

urlpatterns = [
    path('login/', AuthLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout', logoutView, name="logout")
]
