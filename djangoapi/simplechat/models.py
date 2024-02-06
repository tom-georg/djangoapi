from collections.abc import Iterable
from django.db import models


class ChatBeitrag(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'chat_beitrag'
        ordering = ['-created_at']

