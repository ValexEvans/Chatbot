import json
from .models import Conversation


def save_conversation(user_message, bot_response):
    # Create a new conversation if needed or update the latest one
    conversation, created = Conversation.objects.get_or_create(id=1)  # Adjust logic as needed

    # Append the new message to the JSON field
    new_entry = {
        "user": user_message,
        "bot": bot_response
    }

    # Update the messages list
    conversation.messages.append(new_entry)
    conversation.save()

    return conversation
