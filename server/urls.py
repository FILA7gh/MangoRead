from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from server.apps.manga import views as manga_views

router = DefaultRouter()
router.register(r'manga', manga_views.MangaViewSet)
router.register(r'genres', manga_views.GenreViewSet, basename='genres')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/manga/', include('server.apps.manga.urls')),
    path('api/v1/users/', include('server.apps.user.urls')),
    path('api/v1/about-us/', include('server.apps.about_us.urls')),

    path('api/v1/', include(router.urls)),

]
