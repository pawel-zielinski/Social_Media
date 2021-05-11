from django.urls import path
from Post_API import views

app_name = 'Post_API'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('liked/<pk>/', views.liked, name = 'liked'),
    path('disliked/<pk>/', views.disliked, name = 'disliked'),
]
