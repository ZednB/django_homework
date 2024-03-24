from catalog.forms import StyleFormsMixin
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms


class UserRegisterForm(StyleFormsMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
