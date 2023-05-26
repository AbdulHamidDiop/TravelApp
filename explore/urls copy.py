from django.urls import path
from explore.views import Explore
urlpatterns = [
    path('', Explore.as_view(), name = 'explore'),
]