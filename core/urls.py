from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('auth.urls', 'auth'), namespace='auth')),
    path('management/', include(('management.urls',
         'management'), namespace='management')),
    path('', include(('home.urls', 'home'), namespace='home'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
