from django.urls import path
from Post_API import views

app_name = 'Post_API'

urlpatterns = [
    path('', views.home, name = 'home'),
]
