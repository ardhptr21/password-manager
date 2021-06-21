from django import forms
from .models import Account


class ManagementCreateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        widgets = {
            'site_name': forms.TextInput(attrs={'placeholder': 'Site name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.TextInput(attrs={'placeholder': 'password'}),
        }
