from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label='Kullanıcı Adı'
    )

    password1 = forms.CharField(
        label='Şifre',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Şifre Tekrar'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]