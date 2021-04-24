from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'Post_API/home.html', context = {'title' : 'Home Page'})
