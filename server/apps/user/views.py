from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # для запомнить меня
        remember_me = request.data.get('remember_me', False)

        # Создаем токен для пользователя
        refresh = RefreshToken.for_user(user)
        if not remember_me:
            refresh.access_token.set_exp(lifetime=timedelta(minutes=15))
        access_token = str(refresh.access_token)
        user.save()

        return Response(data={'detail': 'Success',
                              'access_token': access_token,
                              'refresh_token': str(refresh)},
                        status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            remember_me = request.data.get('remember_me', False)
            refresh = RefreshToken.for_user(user)
            if not remember_me:
                refresh.access_token.set_exp(lifetime=timedelta(minutes=15))
            access_token = str(refresh.access_token)
            user.save()
            return Response(data={'detail': 'succsess',
                                  'access_token': access_token,
                                  'refresh_token': str(refresh)},
                            status=status.HTTP_201_CREATED
                            )

        return Response(data={'detail': 'Неправильный логин или пароль!'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        # Удаляем refresh_token, чтобы пользователь больше не мог использовать его для аутентификации
        try:
            refresh_token = request.data.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
        except Exception:
            pass

        logout(request)
        return Response(data={'detail': 'Вы успешно вышли'})
