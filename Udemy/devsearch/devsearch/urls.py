from django.contrib import admin
from django.urls import path, include
from django.conf import settings

#Static is basically going to help us create a new url for our static files
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),
]

# We need to add a path to find those uploaded images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# When debug is false django looks for staticfiles
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
