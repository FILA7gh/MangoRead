from rest_framework import serializers
from . import models


class GenreSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)

    class Meta:
        model = models.Genre
        fields = '__all__'


class MangaListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = models.Manga
        fields = ['id', 'image', 'title', 'year', 'genres']


class MangaDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    title = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    year = serializers.DateField()
    sinopsis = serializers.CharField()

    genres = GenreSerializer(many=True)

    class Meta:
        model = models.Manga
        fields = ['id', 'image', 'title', 'type', 'year', 'sinopsis', 'genres']
