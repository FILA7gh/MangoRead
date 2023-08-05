from rest_framework import viewsets
from . import models, serializers, utils, permissions


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all().order_by('id')
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    pagination_class = utils.GenrePagination


class MangaViewSet(viewsets.ModelViewSet):
    queryset = models.Manga.objects.all().order_by('id')
    permission_classes = [permissions.IsAdminOrReadOnly]
    pagination_class = utils.MangaPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MangaListSerializer
        return serializers.MangaDetailSerializer
