from django.contrib import admin
from .models import Traveller, Guide, TravellerPreferences
# Register your models here.
admin.site.register(Traveller)
admin.site.register(Guide)
admin.site.register(TravellerPreferences)