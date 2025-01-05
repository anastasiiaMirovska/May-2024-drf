from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView

from apps.user.serializers import UserSerializer

UserModel = get_user_model() # Робиться для того, щоб можна було використовувати не тільки стандартну модель, а і кастомну
# тобто якщо прописати get_user_model(), то першим ділом воно шукатиме кастомну модель, а потім стандартну from django.contrib.auth.models import User


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    

