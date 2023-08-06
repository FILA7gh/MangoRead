from django.urls import include, path

from . import views


urlpatterns = [
    # reviews
    path('<int:pk>/reviews/', include('server.apps.reviews.urls'))
]
