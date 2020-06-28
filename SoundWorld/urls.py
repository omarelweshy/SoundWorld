from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'SoundWorld API'
API_DESCRIPTION = 'A Web API for creating and editing SoundWorld Data.'
schema_view = get_schema_view(title=API_TITLE)

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

    # APIs
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns