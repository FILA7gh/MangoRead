from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.MangaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', views.MangaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})),

    # genres
    path('genres/' ,views.GenreViewSet.as_view({'get': 'list', 'post': 'create'})),

    # reviews
    path('<int:pk>/reviews/', include('server.apps.reviews.urls'))
]
