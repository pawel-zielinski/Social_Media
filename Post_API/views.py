from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from Login_API.models import UserProfile
from django.contrib.auth.models import User


@login_required
def home(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains = search)
    return render(request, 'Post_API/home.html', context = {'title' : 'Feetbook | Home', 'search' : search, 'result' : result})
