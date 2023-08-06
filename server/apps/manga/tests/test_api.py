from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from server.apps.manga.models import Genre
from server.apps.manga.serializers import GenreSerializer


class GenreAPITestCase(APITestCase):
    def test_get(self):
        genre_1 = Genre.objects.create(title='adventure')
        genre_2 = Genre.objects.create(title='fantasy')
        url = reverse('genres-list')
        response = self.client.get(url)  # ответ
        serializer_data = GenreSerializer([genre_1, genre_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # проверка статуса

        # для пагинации
        self.assertIn('count', response.data)
        self.assertIn('next', response.data)
        self.assertIn('results', response.data)

        # проверка апи
        genres = response.data['results']
        self.assertEqual(genres, serializer_data)

        # добавляем пагинацию
        paginator = Paginator(Genre.objects.all(), 10)

        # проверка на страницу
        self.assertEqual(paginator.num_pages, 1)
