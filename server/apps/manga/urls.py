from rest_framework.urls import path
from . import views

urlpatterns = [
    path('', views.MangaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', views.MangaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})),

    path('genres/' ,views.GenreViewSet.as_view({'get': 'list', 'post': 'create'}))
]
