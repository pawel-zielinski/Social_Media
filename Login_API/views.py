from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data = request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user = user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Login_API:login'))
    return render(request, 'Login_API/signup.html', context = {'title' : 'Sign up from here', 'form' : form})

@login_required
def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse(''))
    return render(request, 'Login_API/login.html', context = {'title' : 'Login Page', 'form' : form})
