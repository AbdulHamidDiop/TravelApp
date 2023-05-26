from django.urls import path
from userprofile.views import Profile

urlpatterns = [
    path('', Profile.as_view(), name = 'profile'),
]