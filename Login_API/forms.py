from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required = True, label = '', widget = forms.TextInput(attrs = {'placeholder' : 'Your Email'}))
    username = forms.CharField(required = True, label = '', widget = forms.TextInput(attrs = {'placeholder' : 'Your Username'}))
    password1 = forms.CharField(required = True, label = '', widget = forms.PasswordInput(attrs = {'placeholder' : 'Your Password'}))
    password2 = forms.CharField(required = True, label = '', widget = forms.PasswordInput(attrs = {'placeholder' : 'Confirm Your Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class FixedAuthenticationForm(AuthenticationForm):
    username = forms.CharField(required = True, label = '', widget = forms.TextInput(attrs = {'placeholder' : 'Your Username'}))
    password = forms.CharField(required = True, label = '', widget = forms.PasswordInput(attrs = {'placeholder' : 'Your Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
