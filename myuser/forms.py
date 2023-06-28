from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    SECTOR_CHOICES = [
        ('vendedor', 'Vendedor'),
        ('produtor', 'Produtor'),
        ('gerencia', 'Gerência'),
    ]
    sector = forms.ChoiceField(choices=SECTOR_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'sector')
