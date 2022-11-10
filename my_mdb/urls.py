from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from user.views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', home_view),
    path('', include('registration.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
