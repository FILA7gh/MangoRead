from rest_framework import serializers
from server.apps.manga.models import Manga
from . import models


class MangaReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['title']


class AvatarReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Avatar
        fields = ['avatar']


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'first_name']


''' Review '''


class ReviewListSerializer(serializers.ModelSerializer):
    avatar = AvatarReviewSerializer()
    text = serializers.CharField()
    user = UserReviewSerializer()
    manga = serializers.PrimaryKeyRelatedField(queryset=Manga.objects.all())

    class Meta:
        model = models.Review
        fields = ['id', 'avatar', 'user', 'manga', 'text']


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    manga = serializers.PrimaryKeyRelatedField(queryset=Manga.objects.all())

    class Meta:
        model = models.Review
        fields = ['manga', 'text']
