from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # ALLAUTH
    path('accounts/', include('allauth.urls')),

    # APPS
    path('', include('pages.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
