from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'f_name', 'l_name', 'condo_name', 'unit_floor', 'unit_unit')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'f_name', 'l_name', 'condo_name', 'unit_floor', 'unit_unit')


class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'f_name', 'l_name', 'condo_name', 'unit_floor', 'unit_unit')