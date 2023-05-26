from django.urls import path
from settings.views import Settings, ProfileSettings
urlpatterns = [
    path('', Settings.as_view(), name = 'settings'),
    path('profile/', ProfileSettings.as_view(), name = 'profilesettings'),
]