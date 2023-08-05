from rest_framework.urls import path

from . import views


urlpatterns = [
    path('', views.AboutUsAPIView.as_view())
]
