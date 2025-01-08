from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

from apps.user.serializers import UserSerializer

UserModel = get_user_model()

class ActivateUserView(GenericAPIView):
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecoverByEmailView(GenericAPIView):
    permission_classes = [AllowAny,]

    def get(self, *args, **kwargs):
        email = kwargs['email']
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        EmailService.recover(user)
        return Response({'message': 'Email sent!'}, status=status.HTTP_200_OK)


class UserRecoveryView(GenericAPIView):
    permission_classes = [AllowAny, ]
    def patch(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, RecoveryToken)
        user.set_password(kwargs['password'])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
