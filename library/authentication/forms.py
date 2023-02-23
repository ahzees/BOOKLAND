from django import forms
from .models import *


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, label="Email")
    password = forms.CharField(max_length=255, label="Password", widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, label="Email")
    password = forms.CharField(max_length=255, label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password', 'password2', 'role']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

