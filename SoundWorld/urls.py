from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Sound World"
admin.site.site_title = "Sound World"
admin.site.index_title = "Welcome to Sound World Admin Panel"

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # ALLAUTH
    path('accounts/', include('allauth.urls')),

    # APPS
    path('', include('pages.urls')),
    path('api/', include('api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
