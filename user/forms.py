from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'text',
        'placeholder': 'Nom d\'utilisateur/email (de base votre nom d\'utilisateur est votre email)',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'text',
        'placeholder': 'Mot de passe',
    }))


class RegisterForm(UserCreationForm):

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'text',
        'placeholder': 'Nom',
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'text',
        'placeholder': 'Prénom',
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'text',
        'placeholder': 'eMail',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'text',
        'placeholder': 'Mot de passe',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'text',
        'placeholder': 'Confirmer le mot de passe',
    }))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'password1', 'password2')

