from django.contrib import admin
from django.urls import path
from .settings.swagger import urlpatterns as swagger
from django.conf.urls.static import static

from server.settings.base import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += swagger