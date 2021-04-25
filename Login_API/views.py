from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateNewUser, FixedAuthenticationForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from .models import UserProfile
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
    return render(request, 'Login_API/signup.html', context = {'title' : 'Feetbook | Sign Up', 'form' : form})

def login_page(request):
    form = FixedAuthenticationForm()
    if request.method == 'POST':
        form = FixedAuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Post_API:home'))
    return render(request, 'Login_API/login.html', context = {'title' : 'Feetbook | Login', 'form' : form})

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user = request.user)
    form = EditProfileForm(instance = current_user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance = current_user)
        if form.is_valid():
            form.save(commit = True)
            form = EditProfileForm(instance = current_user)
            return HttpResponseRedirect(reverse('Login_API:profile'))

    return render(request, 'Login_API/profile.html', context = {'title' : 'Feetbook | Edit Profile', 'form' : form})

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_API:login'))

@login_required
def profile(request):
    return render(request, 'Login_API/user.html', context = {'title' : 'Feetbook | Profile'})
