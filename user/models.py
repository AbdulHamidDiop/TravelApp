from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# Create your models here.
class TravellerPreferences():
    distance = models.CharField(blank=True)
    interest = models.CharField(blank=True)
    partySize = models.SmallIntegerField(blank=True)

class Traveller(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    userID = models.IntegerField()

    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20, blank=True)
    isGuide = models.BooleanField(default=False)
    profilePic = models.ImageField(upload_to='profileImages', default = 'pfp.png')
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    preferences = TravellerPreferences()    
    def __str__(self):
        return self.user.username

class Guide(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    userID = models.IntegerField()

    firstName = models.CharField(max_length=15, blank=True)
    lastName = models.CharField(max_length=15, blank=True)
    telephone = models.TextField()
    
    bio = models.CharField(max_length=200, blank=True)
    profilePic = models.ImageField(upload_to='profileImages', default = 'pfp.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
