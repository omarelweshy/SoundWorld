from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # APPS
    path('users/', include('users.urls')),
    path('pages/', include('pages.urls')),
]
