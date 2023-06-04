from django.urls import path
from userprofile.views import Profile

urlpatterns = [
    path('<str:pk>', Profile.as_view(), name = 'profile'),
]