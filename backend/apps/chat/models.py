from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class ChatRoomModel(models.Model):
    class Meta:
        db_table = 'chat_rooms'

    name = models.CharField(max_length=50)
    is_private = models.BooleanField(default=False)
    users = models.ManyToManyField(UserModel, related_name='chat_rooms')


class ChatMessageModel(models.Model):
    class Meta:
        db_table = 'chat_messages'

    text = models.TextField()
    room = models.ForeignKey(ChatRoomModel, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='messages')

