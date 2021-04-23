from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required = True, label = '', widget = forms.TextInput(attrs = {'placeholder' : 'Your Email'}))
    username = forms.CharField(required = True, label = '', widget = forms.TextInput(attrs = {'placeholder' : 'Your Username'}))
    password1 = forms.CharField(required = True, label = '', widget = forms.PasswordInput(attrs = {'placeholder' : 'Your Password'}))
    password2 = forms.CharField(required = True, label = '', widget = forms.PasswordInput(attrs = {'placeholder' : 'Confirm Your Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
