from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'username', 'password')
    search_fields = ('site_name',)
