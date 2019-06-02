from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import datetime

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'f_name', 'l_name', 'condo_name',
                  'unit_floor', 'unit_unit')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'f_name', 'l_name',
                  'condo_name', 'unit_floor', 'unit_unit', 'is_active',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'f_name', 'l_name',
                  'condo_name', 'unit_floor', 'unit_unit')


# class NameForm(forms.Form):
#     # your_name = forms.CharField(label='Your name', max_length=100)
#     date = forms.DateField(
#         input_formats=['%d/%m/%Y'],
#         widget=forms.DateInput(attrs={
#             'data-target': '#datepicker1'
#         })
#     )
#     time = forms.TimeField(
#         input_formats=['%H:%M'],
#         widget=forms.TimeInput(attrs={
#             'data-target': '#timepicker1'
#         })
#     )
