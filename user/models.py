from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# Create your models here.
class TravellerPreferences(models.Model):
    id = models.AutoField(primary_key=True)
    distance = models.CharField(max_length=1, blank=True, default="0") 
    interests = models.CharField(max_length=1, blank=True, default="0")
    partySize = models.SmallIntegerField(blank=True, default="0")

class Traveller(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20, blank=True)
    isGuide = models.BooleanField(default=False)
    profilePic = models.ImageField(upload_to='profileImages', default = 'pfp.png')
    location = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length = 200,blank=True)

    preferences = models.OneToOneField(TravellerPreferences, on_delete=models.CASCADE, default=1, blank=True)
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
