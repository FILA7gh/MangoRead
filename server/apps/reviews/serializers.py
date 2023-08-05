from rest_framework import serializers
from . import models


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Avatar
        fields = ['avatar']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'first_name']


class ReviewListSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer()
    text = serializers.CharField()
    user = UserSerializer()

    class Meta:
        model = models.Review
        fields = ['id', 'avatar', 'user', 'text']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ['text']
