from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class ChatRoomModel(models.Model):
    class Meta:
        db_table = 'chat_rooms'

    name = models.CharField(max_length=50)


class ChatMessageModel(models.Model):
    class Meta:
        db_table = 'chat_messages'

    text = models.TextField()
    room = models.ForeignKey(ChatRoomModel, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='messages')

