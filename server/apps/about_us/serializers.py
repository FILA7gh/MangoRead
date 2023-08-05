from rest_framework import serializers
from . import models


class AboutUsSerializer(serializers.ModelSerializer):
    tagline = serializers.CharField(max_length=255)
    link_one = serializers.URLField()
    link_two = serializers.URLField()
    link_three = serializers.URLField()
    map = serializers.URLField()

    class Meta:
        model = models.AboutUs
        fields = '__all__'
