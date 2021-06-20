from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('auth.urls', 'auth'), namespace='auth')),
    path('management/', include(('management.urls',
         'management'), namespace='management')),
    path('', include(('home.urls', 'home'), namespace='home'))
]
