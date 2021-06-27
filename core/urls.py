from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path('auth/', include(('auth.urls', 'auth'), namespace='auth')),
    path('management/', include(('management.urls',
         'management'), namespace='management')),
    path('', include(('home.urls', 'home'), namespace='home'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
