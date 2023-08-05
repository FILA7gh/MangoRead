from django.contrib import admin
from django.urls import path, include
from .settings.swagger import urlpatterns as swagger
from django.conf.urls.static import static

from server.settings.base import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/manga/', include('server.apps.manga.urls')),

    path('api/v1/users/', include('server.apps.user.urls')),

    path('api/v1/about-us/', include('server.apps.about_us.urls')),

    path('api/v1/reviews/', include('server.apps.reviews.urls')),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += swagger
