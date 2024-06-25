from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import CustomUser

class LoginForm(AuthenticationForm):
    username = UsernameField(label='Enter username')
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username','email')