from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(
        max_length=100, required=False, initial="")

    lastname = forms.CharField(
        max_length=100, required=False, initial='')

    email = forms.EmailField(required=True, help_text='Required')

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'password1']
