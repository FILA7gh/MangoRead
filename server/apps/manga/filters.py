import django_filters
from .models import Manga
from django.db.models import Q


''' Фильтрация по названию манги и по жанрам '''


class MangaFilter(django_filters.FilterSet):
    title = django_filters.Filter(field_name='title', lookup_expr='icontains')
    genres_title = django_filters.Filter(method='filter_genres_title')

    class Meta:
        model = Manga
        fields = []

    def filter_genres_title(self, queryset, name, value):
        genre_titles = value.split(',')
        q_objects = Q()
        for genre_title in genre_titles:
            q_objects |= Q(genres__title__icontains=genre_title.strip())

        return queryset.filter(q_objects)
