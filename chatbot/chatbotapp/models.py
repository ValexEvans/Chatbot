from django.db import models

class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Conversation(models.Model):
    messages = models.JSONField(default=list)  # Stores user-bot chat history
    created_at = models.DateTimeField(auto_now_add=True)