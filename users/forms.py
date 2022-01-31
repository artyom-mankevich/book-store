import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=30, min_length=3,
                               help_text="Latin lowercase letters, underscores and digits only. At least 3 "
                                         "characters.")
    email = forms.EmailField(required=True, validators=[EmailValidator(message="Email is invalid")])
    first_name = forms.CharField(required=False, help_text="Optional. First letter should be uppercase. Only latin "
                                                           "characters. Example: John.")
    last_name = forms.CharField(required=False, help_text="Optional. First letter should be uppercase. Only latin"
                                                          " characters. Example: Smith.")
    profile_pic = forms.ImageField(required=False, help_text="Image file with size below 2.5 MB")

    def clean_username(self):
        data = self.cleaned_data.get('username')
        if not re.match("^[a-z0-9_]{3,30}$", data):
            raise ValidationError("Username is invalid")
        return data

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if data and not re.match("^[A-Z][a-z]+$", data):
            raise ValidationError("First name is invalid")
        return data

    def clean_last_name(self):
        data = self.cleaned_data.get('last_name')
        if data and not re.match("^[A-Z][a-z]+$", data):
            raise ValidationError("Last name is invalid")
        return data

    def clean_profile_pic(self):
        data = self.cleaned_data.get('profile_pic')
        if data:
            if data.size > 2.5 * 1024 * 1024:
                raise ValidationError("Maximum image size is 2.5 MB")
            return data

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'profile_pic']


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
