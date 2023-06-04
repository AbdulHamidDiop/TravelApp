from django.urls import path
from tripsfeed.views import TripsFeed, PinTripView

urlpatterns = [
    path('', TripsFeed.as_view(), name = 'tripsfeed'),
    path('pintrip/', PinTripView.as_view(), name = 'pintrip'),
]