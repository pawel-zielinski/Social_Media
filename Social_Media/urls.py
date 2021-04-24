from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from Post_API.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Login_API.urls')),
    path('posts/', include('Post_API.urls')),
    path('', home, name = 'home')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
