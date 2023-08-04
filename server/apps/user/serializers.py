from rest_framework import serializers
from django.contrib.auth.models import User
import re
from avatar.models import Avatar


class RegisterSerializer(serializers.Serializer):
    photo = serializers.ImageField()
    username = serializers.CharField(max_length=155, required=True)
    first_name = serializers.CharField(max_length=155, required=True)
    password = serializers.CharField(min_length=8, required=True)
    password_confirm = serializers.CharField(min_length=8, required=True)

    def validate_username(self, username):  # проверка на уникальность имени пользователя
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        return serializers.ValidationError('User already exist!')

    def validate_password(self, password):
        if not re.match("^(?=.*?[a-z])(?=.*?[0-9]).{8,}$", password):
            raise serializers.ValidationError(
                'Пароль должен содержать как минимум одну букву и одну цифру, и быть длиной не менее 8 символов!')

        return password

    def validate(self, attrs):
        # проверка на совпадение паролей
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError('Пароли не совпадают!')

        return attrs

    def create(self, validated_data):
        photo = validated_data.get('photo')
        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        password = validated_data.get('password')
        user = User.objects.create_user(
                                          username=username,
                                          first_name=first_name,
                                          password=password
                                          )
        if photo:
            avatar = Avatar(user=user, primary=True)
            avatar.avatar.save(photo.name, photo, save=True)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4, required=True)
    password = serializers.CharField(min_length=8, required=True)
