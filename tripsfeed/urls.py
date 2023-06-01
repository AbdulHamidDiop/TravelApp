from django.urls import path
from tripsfeed.views import TripsFeed, CreateTrip

urlpatterns = [
    path('', TripsFeed.as_view(), name = 'tripsfeed'),
    path('createtrip/', CreateTrip.as_view(), name = 'createTrip')
]