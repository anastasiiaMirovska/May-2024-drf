import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from core.services.email_service import EmailService

from apps.user.serializers import UserSerializer

UserModel = get_user_model() # Робиться для того, щоб можна було використовувати не тільки стандартну модель, а і кастомну
# тобто якщо прописати get_user_model(), то першим ділом воно шукатиме кастомну модель, а потім стандартну from django.contrib.auth.models import User


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    
class UserToAdminView(GenericAPIView):
    permission_classes = [IsAdminUser,]
    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)
    
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlockUserView(GenericAPIView):
    permission_classes = [IsAdminUser,]

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnBlockUserView(GenericAPIView):
    permission_classes = [IsAdminUser,]

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

#
# class SendEmailTestView(GenericAPIView):
#     permission_classes = [AllowAny,]
#     def get(self, *args, **kwargs):
#         template = get_template('test_email.html')
#         html_content = template.render({'name': 'DJANGO'})
#         msg = EmailMultiAlternatives(
#             subject='Test email',
#             from_email=os.environ.get('EMAIL_HOST_USER'),
#             to=['anastasiia.mirovska@gmail.com'],
#         )
#         msg.attach_alternative(html_content, 'text/html')
#         msg.send()
#         return Response({'message': 'Email sent!'}, status=status.HTTP_200_OK)



