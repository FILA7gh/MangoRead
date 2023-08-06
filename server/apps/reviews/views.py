from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from server.core.paginations import PaginationForTen
from . import models, serializers


class ReviewAPIView(ListCreateAPIView):
    queryset = models.Review.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PaginationForTen

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ReviewListSerializer
        elif self.request.method == 'POST':
            return serializers.ReviewSerializer

    def get_queryset(self):
        manga_id = self.kwargs['pk']
        return models.Review.objects.filter(manga_id=manga_id)

    def perform_create(self, serializer):
        user = self.request.user
        avatar, created = models.Avatar.objects.get_or_create(user=user)
        text = self.request.data.get('text')
        manga_id = self.kwargs['pk']
        serializer.save(user=user, avatar=avatar, text=text, manga_id=manga_id)
