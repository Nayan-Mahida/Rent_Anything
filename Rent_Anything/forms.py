from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import items


class itemsForm(forms.ModelForm):
    class Meta:
        model = items
        fields = '__all__'
        exclude = ['user']

class UserCrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AuthForm(AuthenticationForm):
    password = forms.PasswordInput
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
