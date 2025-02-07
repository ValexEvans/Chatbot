from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Conversation
from .utils import save_conversation  # Assuming function is in utils.py

from django.shortcuts import render, HttpResponse
from .models import ToDoItem

# Create your views here.

def home(request):
    return render(request, "home.html")

def todos(request): 
    items = ToDoItem.objects.all()
    return render(request, "todos.html", {"todos": items })


@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message")

            # Example bot response (Replace with AI logic)
            bot_response = f"I received: {user_message}"

            # Save user and bot messages
            conversation = Conversation.objects.create(messages=[{"user": user_message, "bot": bot_response}])

            return JsonResponse({"bot_response": bot_response, "conversation_id": conversation.id})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)