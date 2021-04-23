from django.urls import path
from Login_API import views

app_name = 'Login_API'

urlpatterns = [
    path('signup/', views.sign_up, name = 'sign_up'),
    path('login/', views.login_page, name = 'login'),
]
