from django.urls import path
from . import views
from .views import chat


urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="todos"),
     path('chat/', chat, name='chat'),  # Endpoint for handling chat messages
]