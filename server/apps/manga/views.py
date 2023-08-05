from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from server.core.paginations import PaginationForTen
from . import models, serializers, utils, permissions, filters


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all().order_by('id')
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    pagination_class = PaginationForTen


class MangaViewSet(viewsets.ModelViewSet):
    queryset = models.Manga.objects.all().order_by('id')
    permission_classes = [permissions.IsAdminOrReadOnly]
    pagination_class = utils.MangaPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.MangaFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MangaListSerializer
        return serializers.MangaDetailSerializer
