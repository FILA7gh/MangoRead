from django.test import TestCase

from server.apps.manga.models import Genre
from server.apps.manga.serializers import GenreSerializer


class GenreSerializerTestCase(TestCase):
    def test_ok(self):
        genre_1 = Genre.objects.create(title='adventure')
        genre_2 = Genre.objects.create(title='fantasy')

        serializer_data = GenreSerializer([genre_1, genre_2], many=True).data
        expected_data = [
            {
                'id': genre_1.id,
                'title': 'adventure'
            },
            {
                'id': genre_2.id,
                'title': 'fantasy'
            }
        ]
        self.assertEqual(expected_data, serializer_data)
