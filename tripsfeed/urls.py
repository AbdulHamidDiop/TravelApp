from django.urls import path
from tripsfeed.views import TripsFeed

urlpatterns = [
    path('', TripsFeed.as_view(), name = 'tripsfeed'),
]