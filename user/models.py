from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# Create your models here.
class TravellerPreferences():
    localTrips = models.BooleanField(blank=True)
    internationalTrips = models.BooleanField(blank=True)
    partySize = models.SmallIntegerField(blank=True)

class Traveller(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    userID = models.IntegerField()

    firstName = models.TextField(blank=True)
    lastName = models.TextField(blank=True)
    
    bio = models.TextField(blank=True)
    profilePic = models.ImageField(upload_to='profileImages', default = 'pfp.png')
    location = models.CharField(max_length=100, blank=True)

    preferences = TravellerPreferences()    
    def __str__(self):
        return self.user.username

class Guide(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    userID = models.IntegerField()

    firstName = models.TextField(blank=True)
    lastName = models.TextField(blank=True)
    
    bio = models.TextField(blank=True)
    profilePic = models.ImageField(upload_to='profileImages', default = 'pfp.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
