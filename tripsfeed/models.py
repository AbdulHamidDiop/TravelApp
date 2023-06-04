from django.db import models
import uuid
import datetime
# Create your models here.
class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    creationDate = models.DateTimeField(default=datetime.datetime.now)

    image = models.ImageField(upload_to='postimages', default='post.jpg')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField(blank=True)
    partySize = models.SmallIntegerField(default=2)
    pins = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    
    isReady = models.BooleanField(default=False)

    def partySizeString(self):
        if self.partySize == 0:
            return "any size"
        elif self.partySize == 1:
            return "1-3"
        elif self.partySize == 2:
            return "4-6"
        elif self.partySize == 3:
            return "7-9"
        elif self.partySize == 4:
            return "10+"
        
    def __str__(self):
        return self.country + " with " + self.user

class PinTrip(models.Model):
    tripID = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username