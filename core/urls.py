from django.urls import path
from core.views import DashBoard, Chats, Posts, Explore, Profile
urlpatterns = [
    path('dashboard/', DashBoard.as_view(), name = 'dashboard'),
    path('chats/', Chats.as_view(), name = 'chats'),
    path('posts/', Posts.as_view(), name = 'posts'),
    path('explore/', Explore.as_view(), name = 'explore'),
    path('profile/', Profile.as_view(), name = 'profile')
]