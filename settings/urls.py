from django.urls import path
from settings.views import Settings
urlpatterns = [
    path('settings/', Settings.as_view(), name = 'settings'),
]