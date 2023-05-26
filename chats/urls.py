from django.urls import path
from chats.views import Chats

urlpatterns = [
    path('', Chats.as_view(), name = 'chats'),
]