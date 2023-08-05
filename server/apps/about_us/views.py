from rest_framework.generics import ListAPIView
from . import models, serializers


class AboutUsAPIView(ListAPIView):
    queryset = models.AboutUs.objects.all()
    serializer_class = serializers.AboutUsSerializer

