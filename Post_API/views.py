from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from Login_API.models import UserProfile, Follow
from django.contrib.auth.models import User
from Post_API.models import Post


@login_required
def home(request):
    following_list = Follow.objects.filter(follower = request.user)
    posts = Post.objects.filter(author__in = following_list.values_list('following'))
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains = search)
    return render(request, 'Post_API/home.html', context = {'title' : 'Feetbook | Home', 'search' : search, 'result' : result, 'posts' : posts})
